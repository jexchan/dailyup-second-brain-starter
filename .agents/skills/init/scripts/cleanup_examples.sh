#!/usr/bin/env bash
#
# cleanup_examples.sh — Deterministic example cleanup helper for the /init skill
#
# Usage (from the Vault root):
#   bash .agents/skills/init/scripts/cleanup_examples.sh --list
#   bash .agents/skills/init/scripts/cleanup_examples.sh --clean --yes

set -euo pipefail

usage() {
  sed -n '2,8p' "$0"
}

find_example_targets() {
  example_targets=()

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
    done < <(find "$root" -depth -name '_EXAMPLE_*' -print0)
  done

  if [[ -d "03_Projects/_Example_Project" ]]; then
    example_targets+=("03_Projects/_Example_Project")
  fi
}

print_example_targets() {
  local target
  for target in "${example_targets[@]}"; do
    printf '%s\n' "$target"
  done
  printf 'TOTAL=%d\n' "${#example_targets[@]}"
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

if [[ "$mode" == "--list" ]]; then
  print_example_targets
  exit 0
fi

if (( confirmed != 1 )); then
  echo "Error: cleanup requires prior user confirmation and the --yes flag." >&2
  exit 2
fi

found=${#example_targets[@]}
removed=0

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

find_example_targets
remaining=${#example_targets[@]}
printf 'SUMMARY found=%d removed=%d remaining=%d\n' "$found" "$removed" "$remaining"

if (( remaining > 0 )); then
  echo "Error: example targets remain after cleanup." >&2
  print_example_targets >&2
  exit 1
fi
