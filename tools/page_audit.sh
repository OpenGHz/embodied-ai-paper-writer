#!/usr/bin/env bash
# page_audit.sh — embodied-ai-paper-writer skill tool.
#
# Reports CoRL-style page-budget compliance for the built PDF: total pages,
# the page on which References begins, and the page on which the Appendix
# begins. Main body = pages 1 .. (References page − 1).
#
# Usage:
#   page_audit.sh [--pdf PATH] [--limit N]
#
# Options:
#   --pdf PATH   PDF to inspect. Default: ./main.pdf
#   --limit N    Main-body page budget. Default: 8 (CoRL 2026).
#   -h, --help   Show this help.

set -uo pipefail

PDF="main.pdf"
LIMIT=8

while [[ $# -gt 0 ]]; do
  case "$1" in
    --pdf) PDF="$2"; shift 2 ;;
    --limit) LIMIT="$2"; shift 2 ;;
    -h|--help) sed -n '2,15p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

[[ -f "$PDF" ]] || { echo "PDF not found: $PDF" >&2; exit 1; }

total=$(pdfinfo "$PDF" | awk '/^Pages:/ {print $2}')

# Find first page whose extracted text starts with "References" or "Appendix" (case-insensitive,
# allowing leading whitespace / line numbers from lineno package).
find_first_page() {
  local regex="$1"
  local p hit
  for ((p=1; p<=total; p++)); do
    hit=$(pdftotext -layout -f "$p" -l "$p" "$PDF" - 2>/dev/null \
            | grep -cE "$regex")
    if [[ "${hit:-0}" != "0" ]]; then
      echo "$p"; return 0
    fi
  done
  echo "-"
}

# "References" heading: line number + word "References".
refs_page=$(find_first_page "^[[:space:]]*[0-9]*[[:space:]]+References\b")
# CoRL/NeurIPS appendices are typeset with \appendix which renumbers \section as
# A, B, C, … . Detect the first page bearing a single-letter "A   <Title>" header.
app_page=$(find_first_page "^[[:space:]]*[0-9]*[[:space:]]+A[[:space:]]{2,}[A-Z][a-zA-Z]")

if [[ "$refs_page" == "-" ]]; then
  body_end="$total"
else
  body_end=$((refs_page - 1))
fi

printf "PDF:            %s\n" "$PDF"
printf "Total pages:    %s\n" "$total"
printf "References at:  p%s\n" "$refs_page"
printf "Appendix at:    p%s\n" "$app_page"
printf "Main body ends: p%s   (limit %s)\n" "$body_end" "$LIMIT"

if (( body_end > LIMIT )); then
  printf "STATUS: OVER by %d page(s)\n" "$((body_end - LIMIT))"
  exit 1
else
  printf "STATUS: within budget (%d/%d)\n" "$body_end" "$LIMIT"
fi
