#!/usr/bin/env python3
"""Remove template-example references from the README files that document them."""

from pathlib import Path
import re


def update(path: str, transform) -> None:
    file = Path(path)
    if not file.exists():
        return

    original = file.read_text(encoding="utf-8")
    revised = transform(original)
    if revised != original:
        file.write_text(revised, encoding="utf-8")
        print(f"UPDATED={path}")


def root_readme(text: str) -> str:
    return text.replace(
        "主题默认从一个文件开始，不预建复杂子目录。模板保留 "
        "`_EXAMPLE_Learning_Science.md` 展示主题地图的写法；"
        "初始化个人 Vault 时可通过 `/init` 清理。",
        "主题默认从一个文件开始，不预建复杂子目录。",
    )


def projects_readme(text: str) -> str:
    return text.replace(
        "├── _Example_Project/\n"
        "│   └── Project.md       # 单页示例项目\n",
        "",
    )


def cards_readme(text: str) -> str:
    lines = text.splitlines(keepends=True)
    revised: list[str] = []
    in_type_table = False

    for line in lines:
        if line.startswith("| 类型 | 用途 | 示例卡片 |"):
            revised.append("| 类型 | 用途 |\n")
            in_type_table = True
            continue
        if in_type_table and line.startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 2:
                revised.append(f"| {cells[0]} | {cells[1]} |\n")
                continue
        if in_type_table:
            in_type_table = False
        revised.append(line)

    text = "".join(revised)
    text = text.replace("\n示例卡片统一带 `_EXAMPLE_` 前缀，方便批量删除。\n", "\n")
    return re.sub(
        r"\n## 示例卡片说明\n\n"
        r"本目录预置了 6 张示例卡片（`_EXAMPLE_` 前缀），展示不同类型的卡片长什么样，它们之间怎么互相引用。\n\n"
        r"\*\*你可以安全删除所有 `_EXAMPLE_\*` 文件\*\*，它们只是样板。\n?",
        "\n",
        text,
    )


def topics_readme(text: str) -> str:
    return re.sub(
        r"\n## 示例\n\n"
        r"- \[\[_EXAMPLE_Learning_Science\]\] — 展示长期主题地图如何连接问题、卡片、项目与来源\n\n"
        r"初始化个人 Vault 时，运行 `/init` 可在确认后清理 `_EXAMPLE_\*` 示例文件。\n?",
        "\n",
        text,
    )


def main() -> None:
    update("README.md", root_readme)
    update("03_Projects/README.md", projects_readme)
    update("04_Knowledge/00_Cards/README.md", cards_readme)
    update("04_Knowledge/01_Topics/README.md", topics_readme)


if __name__ == "__main__":
    main()
