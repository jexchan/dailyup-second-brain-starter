#!/usr/bin/env python3
"""Lightweight spaced repetition manager for Obsidian card notes."""

from __future__ import annotations

import argparse
import math
import re
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


CARD_DIR = Path("04_Knowledge/00_Cards")
RATING_VALUES = {"again", "hard", "good", "easy"}
PRIORITY_RANK = {"core": 0, "normal": 1, "low": 2}


@dataclass
class Card:
    path: Path
    frontmatter: Dict[str, str]
    body: str

    @property
    def name(self) -> str:
        return self.path.stem


def parse_date(value: Optional[str]) -> Optional[date]:
    if not value:
        return None
    try:
        return datetime.strptime(str(value).strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def as_bool(value: Optional[str]) -> bool:
    return str(value).strip().lower() in {"true", "yes", "1"}


def as_float(value: Optional[str], default: float) -> float:
    try:
        return float(str(value).strip())
    except (TypeError, ValueError):
        return default


def as_int(value: Optional[str], default: int) -> int:
    try:
        return int(float(str(value).strip()))
    except (TypeError, ValueError):
        return default


def read_card(path: Path) -> Card:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return Card(path=path, frontmatter={}, body=text)

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return Card(path=path, frontmatter={}, body=text)

    raw_fm = parts[1]
    body = parts[2]
    frontmatter: Dict[str, str] = {}
    for line in raw_fm.splitlines():
        if not line.strip() or line.startswith((" ", "\t", "-")):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()

    return Card(path=path, frontmatter=frontmatter, body=body)


def replace_or_add_frontmatter(text: str, updates: Dict[str, str]) -> str:
    if not text.startswith("---\n"):
        lines = ["---", *[f"{key}: {value}" for key, value in updates.items()], "---", ""]
        return "\n".join(lines) + text

    parts = text.split("---\n", 2)
    raw_fm = parts[1]
    body = parts[2]
    lines = raw_fm.splitlines()
    seen = set()
    output = []

    for line in lines:
        match = re.match(r"^([A-Za-z0-9_-]+):(.*)$", line)
        if match and match.group(1) in updates:
            key = match.group(1)
            output.append(f"{key}: {updates[key]}")
            seen.add(key)
        else:
            output.append(line)

    for key, value in updates.items():
        if key not in seen:
            output.append(f"{key}: {value}")

    return "---\n" + "\n".join(output).rstrip() + "\n---\n" + body


def write_frontmatter_updates(path: Path, updates: Dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    path.write_text(replace_or_add_frontmatter(text, updates), encoding="utf-8")


def iter_cards(vault: Path) -> Iterable[Card]:
    card_root = vault / CARD_DIR
    for path in sorted(card_root.glob("*.md")):
        yield read_card(path)


def resolve_card_path(vault: Path, path_argument: str) -> Path:
    card_root = (vault / CARD_DIR).resolve()
    path = (vault / path_argument).resolve()
    try:
        path.relative_to(card_root)
    except ValueError:
        raise SystemExit(f"Card path must be inside: {card_root}")

    if path.parent != card_root or path.suffix.lower() != ".md":
        raise SystemExit(f"Card path must be a Markdown file directly under: {card_root}")
    if not path.exists():
        raise SystemExit(f"Card not found: {path}")
    return path


def due_cards(vault: Path, today: date) -> List[Card]:
    cards = []
    for card in iter_cards(vault):
        fm = card.frontmatter
        if not as_bool(fm.get("srs_enabled")):
            continue
        if fm.get("srs_status", "learning") == "suspended":
            continue
        due = parse_date(fm.get("srs_due"))
        if due and due <= today:
            cards.append(card)

    def sort_key(card: Card) -> Tuple[date, int, int, str]:
        fm = card.frontmatter
        return (
            parse_date(fm.get("srs_due")) or today,
            PRIORITY_RANK.get(fm.get("srs_priority", "normal"), 1),
            -as_int(fm.get("srs_interval"), 1),
            card.name,
        )

    return sorted(cards, key=sort_key)


def format_due(cards: List[Card], today: date, limit: int) -> str:
    if not cards:
        return f"今日没有到期卡片。date={today.isoformat()}"

    rows = [f"今日到期卡片：{len(cards)} 张，显示前 {min(limit, len(cards))} 张。\n"]
    for index, card in enumerate(cards[:limit], start=1):
        fm = card.frontmatter
        rows.append(
            "\n".join(
                [
                    f"{index}. [[{card.name}]]",
                    f"   path: {card.path}",
                    f"   type: {fm.get('card_type', '')}",
                    f"   priority: {fm.get('srs_priority', 'normal')}",
                    f"   due: {fm.get('srs_due', '')}",
                    f"   last: {fm.get('srs_last_reviewed', '')}",
                    f"   interval: {fm.get('srs_interval', '1')} days",
                    f"   reps/lapses: {fm.get('srs_reps', '0')}/{fm.get('srs_lapses', '0')}",
                ]
            )
        )
    return "\n".join(rows)


def enroll(vault: Path, relative_path: str, priority: str, today: date) -> None:
    path = resolve_card_path(vault, relative_path)

    updates = {
        "srs_enabled": "true",
        "srs_status": "learning",
        "srs_due": (today + timedelta(days=1)).isoformat(),
        "srs_last_reviewed": "",
        "srs_interval": "1",
        "srs_ease": "2.5",
        "srs_reps": "0",
        "srs_lapses": "0",
        "srs_priority": priority,
    }
    write_frontmatter_updates(path, updates)
    print(f"Enrolled: {relative_path}")
    print(f"Next due: {updates['srs_due']}")


def next_schedule(fm: Dict[str, str], rating: str) -> Tuple[int, float, int, int, str]:
    interval = as_int(fm.get("srs_interval"), 1)
    ease = max(1.3, as_float(fm.get("srs_ease"), 2.5))
    reps = as_int(fm.get("srs_reps"), 0)
    lapses = as_int(fm.get("srs_lapses"), 0)

    if rating == "again":
        interval = 1
        ease = max(1.3, ease - 0.2)
        lapses += 1
        status = "learning"
    elif rating == "hard":
        interval = max(1, math.ceil(interval * 1.2))
        ease = max(1.3, ease - 0.15)
        reps += 1
        status = "review"
    elif rating == "good":
        interval = max(1, math.ceil(interval * ease))
        reps += 1
        status = "review"
    elif rating == "easy":
        interval = max(2, math.ceil(interval * ease * 1.35))
        ease = ease + 0.15
        reps += 1
        status = "review"
    else:
        raise SystemExit(f"Unsupported rating: {rating}")

    return interval, ease, reps, lapses, status


def append_review_log(path: Path, reviewed_on: date, rating: str, due: date, interval: int, note: str) -> None:
    text = path.read_text(encoding="utf-8")
    section = "\n\n## SRS Review Log\n"
    if "## SRS Review Log" not in text:
        text = text.rstrip() + section
    note_text = f" — {note}" if note else ""
    text = text.rstrip() + f"\n- {reviewed_on.isoformat()} `{rating}` -> {due.isoformat()} ({interval}d){note_text}\n"
    path.write_text(text, encoding="utf-8")


def review(vault: Path, relative_path: str, rating: str, today: date, note: str) -> None:
    if rating not in RATING_VALUES:
        raise SystemExit(f"Rating must be one of: {', '.join(sorted(RATING_VALUES))}")

    path = resolve_card_path(vault, relative_path)
    card = read_card(path)
    if not as_bool(card.frontmatter.get("srs_enabled")):
        raise SystemExit("Card is not enrolled. Run enroll before recording a review.")
    interval, ease, reps, lapses, status = next_schedule(card.frontmatter, rating)
    due = today + timedelta(days=interval)
    updates = {
        "srs_enabled": "true",
        "srs_status": status,
        "srs_due": due.isoformat(),
        "srs_last_reviewed": today.isoformat(),
        "srs_interval": str(interval),
        "srs_ease": f"{ease:.2f}",
        "srs_reps": str(reps),
        "srs_lapses": str(lapses),
    }
    write_frontmatter_updates(path, updates)
    append_review_log(path, today, rating, due, interval, note)
    print(f"Reviewed: {relative_path}")
    print(f"Rating: {rating}")
    print(f"Next due: {due.isoformat()} ({interval} days)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manage spaced repetition for Obsidian cards.")
    parser.add_argument("--vault", default=".", help="Vault root path. Defaults to current directory.")
    parser.add_argument("--date", default=date.today().isoformat(), help="Override today, YYYY-MM-DD.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    due_parser = subparsers.add_parser("due", help="List cards due for review.")
    due_parser.add_argument("--limit", type=int, default=20)

    enroll_parser = subparsers.add_parser("enroll", help="Enroll a card into spaced review.")
    enroll_parser.add_argument("path", help="Card path relative to vault root.")
    enroll_parser.add_argument("--priority", choices=["core", "normal", "low"], default="normal")

    review_parser = subparsers.add_parser("review", help="Record review feedback for a card.")
    review_parser.add_argument("path", help="Card path relative to vault root.")
    review_parser.add_argument("--rating", choices=sorted(RATING_VALUES), required=True)
    review_parser.add_argument("--note", default="")

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    vault = Path(args.vault).resolve()
    today = parse_date(args.date)
    if today is None:
        raise SystemExit("--date must be YYYY-MM-DD")

    if args.command == "due":
        print(format_due(due_cards(vault, today), today, args.limit))
    elif args.command == "enroll":
        enroll(vault, args.path, args.priority, today)
    elif args.command == "review":
        review(vault, args.path, args.rating, today, args.note)


if __name__ == "__main__":
    main()
