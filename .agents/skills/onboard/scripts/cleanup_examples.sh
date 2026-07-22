#!/usr/bin/env bash
#
# cleanup_examples.sh — Deterministic example cleanup helper for the /onboard skill
#
# Usage (from the Vault root):
#   bash .agents/skills/onboard/scripts/cleanup_examples.sh --list
#   bash .agents/skills/onboard/scripts/cleanup_examples.sh --clean --yes

set -euo pipefail

usage() {
  sed -n '2,8p' "$0"
}

find_example_targets() {
  example_targets=()
  example_count=0

  local root target
  for root in \
    "02_Daily" \
    "04_Knowledge/00_Cards" \
    "04_Knowledge/01_Topics" \
    "05_References/01_Inbox"
  do
    [[ -d "$root" ]] || continue
    while IFS= read -r -d '' target; do
      example_targets+=("$target")
      example_count=$((example_count + 1))
    done < <(find "$root" -depth -name '_EXAMPLE_*' -print0)
  done

  if [[ -d "03_Projects/_Example_Project" ]]; then
    example_targets+=("03_Projects/_Example_Project")
    example_count=$((example_count + 1))
  fi
}

find_readme_targets() {
  readme_targets=()
  readme_count=0

  local readme
  for readme in \
    "README.md" \
    "03_Projects/README.md" \
    "04_Knowledge/00_Cards/README.md" \
    "04_Knowledge/01_Topics/README.md"
  do
    [[ -f "$readme" ]] || continue
    if grep -Eq '_EXAMPLE_|_Example_Project' "$readme"; then
      readme_targets+=("$readme")
      readme_count=$((readme_count + 1))
    fi
  done
}

print_cleanup_targets() {
  local target
  if (( example_count > 0 )); then
    for target in "${example_targets[@]}"; do
      printf 'DELETE=%s\n' "$target"
    done
  fi
  if (( readme_count > 0 )); then
    for target in "${readme_targets[@]}"; do
      printf 'UPDATE=%s\n' "$target"
    done
  fi
  printf 'EXAMPLE_TOTAL=%d\n' "$example_count"
  printf 'README_TOTAL=%d\n' "$readme_count"
  printf 'TOTAL=%d\n' "$((example_count + readme_count))"
}

mode=""
confirmed=0

for arg in "$@"; do
  case "$arg" in
    --list|--clean)
      if [[ -n "$mode" && "$mode" != "$arg" ]]; then
        echo "Error: choose exactly one mode." >&2
        usage >&2
        exit 2
      fi
      mode="$arg"
      ;;
    -y|--yes)
      confirmed=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Error: unknown argument: $arg" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ ! -f "CLAUDE.md" || ! -d "04_Knowledge/00_Cards/.templates" ]]; then
  echo "Error: run this helper from the Vault root directory." >&2
  exit 1
fi

if [[ -z "$mode" ]]; then
  echo "Error: choose --list or --clean." >&2
  usage >&2
  exit 2
fi

find_example_targets
find_readme_targets

if [[ "$mode" == "--list" ]]; then
  print_cleanup_targets
  exit 0
fi

if (( confirmed != 1 )); then
  echo "Error: cleanup requires prior user confirmation and the --yes flag." >&2
  exit 2
fi

found=$example_count
removed=0
readmes_found=$readme_count

if (( found > 0 )); then
  for target in "${example_targets[@]}"; do
    if [[ -d "$target" ]]; then
      rm -rf -- "$target"
    elif [[ -e "$target" ]]; then
      rm -- "$target"
    else
      continue
    fi
    removed=$((removed + 1))
    printf 'REMOVED=%s\n' "$target"
  done
fi

if (( readmes_found > 0 )); then
  python3 "$(dirname "$0")/cleanup_readme_refs.py"
fi

find_example_targets
find_readme_targets
remaining=$example_count
readmes_remaining=$readme_count
printf 'SUMMARY examples_found=%d examples_removed=%d examples_remaining=%d readmes_updated=%d readmes_remaining=%d\n' \
  "$found" "$removed" "$remaining" "$readmes_found" "$readmes_remaining"

if (( remaining > 0 || readmes_remaining > 0 )); then
  echo "Error: example files or related README references remain after cleanup." >&2
  print_cleanup_targets >&2
  exit 1
fi
