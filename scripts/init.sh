#!/usr/bin/env bash
#
# init.sh — Initialize a fresh Vault from this starter template
#
# What it does:
#   1. Removes all _EXAMPLE_* files (example daily notes, cards, clippings)
#   2. Removes the _Example_Project/ directory
#   3. Optionally rewrites CLAUDE.md / AGENTS.md placeholders with your name
#   4. Creates the first Daily Note for today
#   5. Reminds you to fill in 01_Context/ files
#
# Usage:
#   bash scripts/init.sh            # interactive mode
#   bash scripts/init.sh --yes      # non-interactive, accept all defaults
#
# Safe to re-run: already-cleaned files are silently skipped.

set -euo pipefail

# ------------- helpers -------------
color() { printf '\033[%sm%s\033[0m' "$1" "$2"; }
green() { color "1;32" "$1"; }
yellow() { color "1;33" "$1"; }
red()   { color "1;31" "$1"; }
bold()  { color "1"    "$1"; }

confirm() {
  local prompt="$1"
  if [[ "${YES:-0}" == "1" ]]; then
    return 0
  fi
  read -r -p "$(yellow "$prompt") [y/N] " ans
  [[ "$ans" =~ ^[Yy]$ ]]
}

YES=0
for arg in "$@"; do
  case "$arg" in
    -y|--yes) YES=1 ;;
    -h|--help)
      sed -n '2,17p' "$0"
      exit 0
      ;;
  esac
done

# ------------- sanity check -------------
if [[ ! -f "CLAUDE.md" || ! -d "04_Knowledge/00_Cards/.templates" ]]; then
  echo "$(red '✗') You must run this script from the Vault root directory."
  exit 1
fi

echo
bold "== DailyUp Second Brain Starter — init =="
echo

# ------------- step 1: remove example files -------------
echo "$(bold 'Step 1:') remove example files"
removed=0

for pat in \
  "02_Daily/_EXAMPLE_*.md" \
  "04_Knowledge/00_Cards/_EXAMPLE_*.md" \
  "05_References/01_Inbox/_EXAMPLE_*.md"
do
  for f in $pat; do
    [[ -e "$f" ]] || continue
    if confirm "  delete $f ?"; then
      rm "$f"
      removed=$((removed + 1))
      echo "  $(green '✓') removed $f"
    fi
  done
done

if [[ -d "03_Projects/_Example_Project" ]]; then
  if confirm "  delete 03_Projects/_Example_Project/ ?"; then
    rm -rf 03_Projects/_Example_Project
    removed=$((removed + 1))
    echo "  $(green '✓') removed 03_Projects/_Example_Project/"
  fi
fi

echo "  → $removed example(s) removed"
echo

# ------------- step 2: first Daily Note -------------
echo "$(bold 'Step 2:') create today's Daily Note"
today="$(date +%Y-%m-%d)"
daily_file="02_Daily/${today}.md"
template="02_Daily/.templates/Daily_Note.md"

if [[ -f "$daily_file" ]]; then
  echo "  $(yellow '!') $daily_file already exists, skipping"
elif [[ ! -f "$template" ]]; then
  echo "  $(red '✗') template $template not found, skipping"
else
  if confirm "  create $daily_file from template ?"; then
    sed "s/{{YYYY-MM-DD}}/$today/g" "$template" > "$daily_file"
    echo "  $(green '✓') created $daily_file"
  fi
fi
echo

# ------------- step 3: reminders -------------
echo "$(bold 'Step 3:') next steps"
echo
echo "  📝 Please fill in your personal context:"
for f in About_Me Mission_and_Vision Brand_Voice Audience_Profiles Current_Priorities; do
  if [[ -f "01_Context/$f.md" ]]; then
    echo "     • 01_Context/$f.md"
  fi
done
echo
echo "  🤖 Then open Claude Code / Codex / Cursor and run:"
echo "     /session-brief    → let AI understand your Vault"
echo "     /today            → generate today's plan"
echo "     /card-creator     → create your first knowledge card"
echo
echo "$(green '✓') init complete."
echo
echo "Read $(bold QUICK_START.md) for the full onboarding guide."
