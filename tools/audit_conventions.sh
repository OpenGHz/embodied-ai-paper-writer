#!/usr/bin/env bash
# audit_conventions.sh — embodied-ai-paper-writer skill tool.
#
# Generic LaTeX paper convention auditor. Reads main.tex, follows every
# \input{...} (recursively, one extra level deep), and runs the SKILL.md
# rule-derived sweeps over every actually-included .tex file.
#
# Designed to be invoked from any paper directory without modification.
# Project-specific patterns (the paper's old/locked names, scope-tag
# modifiers, etc.) live in an optional config file that the paper owns.
#
# Usage:
#   audit_conventions.sh [options]
#
# Options:
#   --paper-dir DIR    Directory containing main.tex. Default: current dir.
#   --main FILE        Top-level LaTeX file relative to paper-dir.
#                      Default: main.tex (falls back to paper.tex if missing).
#   --check LIST       Comma-separated list of sweeps to run.
#                      Default: all available.
#                      Examples: --check r14,r16
#                                --check r18,r20
#   --config FILE      Path to project-specific config file. Default:
#                      <paper-dir>/audit_conventions.conf if present.
#   --strict           Exit 1 if any sweep finds something.
#   --list             List available sweeps and exit.
#   -h, --help         Show this help.
#
# Available sweeps:
#   r02           — System-name spelling drift (needs config: RULE_02_OLD_NAMES)
#   r14           — Abstract self-containment + method-internal jargon
#                    (abstract file only; universal patterns)
#   r16           — Table jargon (`row`/`column`/`cell`) in prose
#                    (universal; manually verify each hit is table-anchored)
#   r18           — Paired condition labels — orphan use of OLD names
#                    (needs config: RULE_18_OLD_LABELS)
#   r19           — Writing-process archaeology (E0N, Phase N, "originally
#                    we used", "most conservative of the candidates", etc.)
#                    (universal)
#   r20           — Load-bearing scope-tag modifier outside its definition
#                    (needs config: RULE_20_MODIFIER, RULE_20_DEFINITION_FILE)
#   vocab-lock    — Project-specific vocabulary locks; the auditor surfaces
#                    every occurrence for manual verification (some hits may
#                    be legitimate source statements / external citations)
#                    (needs config: VOCAB_LOCK_PATTERNS)
#   comparator    — `comparator`/`comparators`/`comparative method` →
#                    `baseline` (universal vocabulary lock)
#   refs          — Orphan \ref / \autoref / \Cref / \pageref / \eqref
#                    targets pointing to non-existent labels (universal)
#   orphan-files  — .tex files in sections/ or figures/ NOT \input'd by the
#                    build (likely stale)
#
# Config file schema (Bash-sourced; see tools/audit_conventions.example.conf):
#   RULE_02_OLD_NAMES=("Old System Name 1" "Old System Name 2")
#   RULE_18_OLD_LABELS=("iteration row" "no-prompt baseline")
#   RULE_20_MODIFIER="successful"
#   RULE_20_DEFINITION_FILE="sections/3_method.tex"
#   # Optional: extra patterns to scan, in addition to universal ones
#   EXTRA_R19_PATTERNS=("Within-run baseline" "E02 baseline")

set -uo pipefail

# ----------------------------------------------------------------------------
# CLI parsing
# ----------------------------------------------------------------------------
PAPER_DIR="."
MAIN_FILE=""
CHECKS_LIST=""
CONFIG_FILE=""
STRICT=0
LIST_ONLY=0

print_help() { sed -n '2,/^set -uo/p' "$0" | sed 's/^# \{0,1\}//' | head -n -1; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    --paper-dir) PAPER_DIR="$2"; shift 2 ;;
    --main) MAIN_FILE="$2"; shift 2 ;;
    --check) CHECKS_LIST="$2"; shift 2 ;;
    --config) CONFIG_FILE="$2"; shift 2 ;;
    --strict) STRICT=1; shift ;;
    --list) LIST_ONLY=1; shift ;;
    -h|--help) print_help; exit 0 ;;
    *) echo "unknown arg: $1" >&2; print_help >&2; exit 2 ;;
  esac
done

ALL_CHECKS=(r02 r14 r16 r18 r19 r20 vocab-lock comparator refs orphan-files)
if ((LIST_ONLY)); then
  printf '%s\n' "${ALL_CHECKS[@]}"; exit 0
fi

cd "$PAPER_DIR" || { echo "no such dir: $PAPER_DIR" >&2; exit 2; }

# Auto-locate main.tex
if [[ -z "$MAIN_FILE" ]]; then
  if [[ -f "main.tex" ]]; then MAIN_FILE="main.tex"
  elif [[ -f "paper.tex" ]]; then MAIN_FILE="paper.tex"
  else
    # last resort: pick the first .tex that declares \documentclass
    MAIN_FILE=$(grep -lE '^\s*\\documentclass' *.tex 2>/dev/null | head -1)
  fi
fi
if [[ -z "$MAIN_FILE" || ! -f "$MAIN_FILE" ]]; then
  echo "no main .tex file found (tried main.tex, paper.tex, \\documentclass scan)" >&2
  exit 2
fi

# Auto-locate config
if [[ -z "$CONFIG_FILE" && -f "audit_conventions.conf" ]]; then
  CONFIG_FILE="audit_conventions.conf"
fi

# Source config if provided (sets project-specific patterns)
RULE_02_OLD_NAMES=()
RULE_18_OLD_LABELS=()
RULE_20_MODIFIER=""
RULE_20_DEFINITION_FILE=""
EXTRA_R19_PATTERNS=()
VOCAB_LOCK_PATTERNS=()
if [[ -n "$CONFIG_FILE" && -f "$CONFIG_FILE" ]]; then
  # shellcheck disable=SC1090
  source "$CONFIG_FILE"
fi

# Pick which checks to run
if [[ -z "$CHECKS_LIST" || "$CHECKS_LIST" == "all" ]]; then
  ACTIVE_CHECKS=("${ALL_CHECKS[@]}")
else
  IFS=',' read -r -a ACTIVE_CHECKS <<< "$CHECKS_LIST"
fi

has_check() {
  local target="$1" c
  for c in "${ACTIVE_CHECKS[@]}"; do [[ "$c" == "$target" ]] && return 0; done
  return 1
}

# ----------------------------------------------------------------------------
# \input discovery (recursive, one extra level deep)
# ----------------------------------------------------------------------------
discover_inputs() {
  local seeds=("$MAIN_FILE")
  local seen=()
  local queue=("${seeds[@]}")
  while ((${#queue[@]})); do
    local f="${queue[0]}"
    queue=("${queue[@]:1}")
    [[ ! -f "$f" ]] && continue
    local s found=0
    for s in "${seen[@]:-}"; do [[ "$s" == "$f" ]] && found=1 && break; done
    ((found)) && continue
    seen+=("$f")
    while IFS= read -r raw; do
      local cand="$raw"
      [[ "$cand" != *.tex ]] && cand="${cand}.tex"
      queue+=("$cand")
    done < <(grep -hoE '\\(input|include)\{[^}]+\}' "$f" 2>/dev/null \
              | sed -E 's/\\(input|include)\{([^}]+)\}/\2/')
  done
  printf '%s\n' "${seen[@]}"
}

mapfile -t FILES < <(discover_inputs)

# Filter: drop main.tex (just \input chain) and math_commands.tex (pure macros)
PROSE_FILES=()
for f in "${FILES[@]}"; do
  [[ "$f" == "$MAIN_FILE" ]] && continue
  [[ "$f" == *math_commands.tex || "$f" == *math_*.tex || "$f" == *macros*.tex ]] && continue
  [[ ! -f "$f" ]] && continue
  PROSE_FILES+=("$f")
done

# Orphan files: present in sections/ or figures/ but NOT in FILES
ORPHANS=()
while IFS= read -r f; do
  local_seen=0
  for kept in "${FILES[@]}"; do
    [[ "$kept" == "$f" ]] && local_seen=1 && break
  done
  ((local_seen)) || ORPHANS+=("$f")
done < <(find -L sections figures -name '*.tex' 2>/dev/null | sort)

# Detect abstract file (any file matching *abstract*.tex)
ABSTRACT_FILE=""
for f in "${PROSE_FILES[@]}"; do
  if [[ "$f" == *abstract* ]]; then ABSTRACT_FILE="$f"; break; fi
done

# ----------------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------------
echo "=== audit_conventions.sh (embodied-ai-paper-writer skill tool) ==="
echo "Paper dir: $(pwd)"
echo "Main: $MAIN_FILE"
[[ -n "$CONFIG_FILE" ]] && echo "Config: $CONFIG_FILE" || echo "Config: (none — project-specific sweeps will be skipped)"
echo "Active sweeps: ${ACTIVE_CHECKS[*]}"
echo "Discovered \\input'd files (${#PROSE_FILES[@]}):"
printf '  %s\n' "${PROSE_FILES[@]}"
if ((${#ORPHANS[@]})); then
  echo
  echo "Orphan .tex files (present but NOT \\input'd by build):"
  printf '  %s\n' "${ORPHANS[@]}"
fi
echo

# ----------------------------------------------------------------------------
# Sweep helpers
# ----------------------------------------------------------------------------
hits=0
skips=0

sweep_print_header() { echo "--- [$1] ---"; }
sweep_print_clean() { echo "(clean)"; echo; }
sweep_print_skipped() {
  echo "(skipped — needs config: $1)"
  echo
  skips=$((skips + 1))
}
sweep_print_findings() {
  echo "$1"
  echo
  hits=$((hits + 1))
}

grep_all() {
  # grep pattern (ERE) over PROSE_FILES; quietly tolerate empty results
  grep -nHE "$1" "${PROSE_FILES[@]}" 2>/dev/null || true
}

grep_all_fixed() {
  # grep -F fixed strings over PROSE_FILES. Pass each pattern as a separate arg.
  local args=()
  local p
  for p in "$@"; do args+=("-e" "$p"); done
  grep -nHF "${args[@]}" "${PROSE_FILES[@]}" 2>/dev/null || true
}

# ----------------------------------------------------------------------------
# Sweeps
# ----------------------------------------------------------------------------

# R02 — system-name spelling drift (config-driven; literal strings)
if has_check r02; then
  sweep_print_header "R02 — system-name spelling drift"
  if ((${#RULE_02_OLD_NAMES[@]} == 0)); then
    sweep_print_skipped "RULE_02_OLD_NAMES in config"
  else
    out=$(grep_all_fixed "${RULE_02_OLD_NAMES[@]}")
    if [[ -n "$out" ]]; then sweep_print_findings "$out"; else sweep_print_clean; fi
  fi
fi

# R14 — abstract self-containment + method-internal jargon (universal)
if has_check r14; then
  sweep_print_header "R14 — abstract self-containment + method-internal jargon"
  if [[ -z "$ABSTRACT_FILE" ]]; then
    sweep_print_skipped "no *abstract*.tex found"
  else
    pattern='\\ref\{|\\autoref|\\Cref|\b[Ss]ection [0-9]|\bFig\.|\bTable |\bgate\b|\bcommit\b|\bconverge|\bepoch\b|early stopping|\biteration\b'
    out=$(grep -nHE "$pattern" "$ABSTRACT_FILE" 2>/dev/null || true)
    if [[ -n "$out" ]]; then sweep_print_findings "$out"; else sweep_print_clean; fi
  fi
fi

# R16 — table jargon in prose (universal; needs human verification)
if has_check r16; then
  sweep_print_header "R16 — 'row'/'rows'/'column'/'cell' in prose (manually verify each is table-anchored)"
  # Skip the figure/table tex files themselves where 'row' is expected
  filtered_files=()
  for f in "${PROSE_FILES[@]}"; do
    [[ "$f" == *table*.tex || "$f" == *tab_*.tex ]] && continue
    filtered_files+=("$f")
  done
  out=$(grep -nHE '\brow\b|\brows\b|\bcolumn\b|\bcell\b' "${filtered_files[@]}" 2>/dev/null || true)
  if [[ -n "$out" ]]; then sweep_print_findings "$out"; else sweep_print_clean; fi
fi

# R18 — paired condition labels: orphan use of OLD names (config-driven; literal strings)
if has_check r18; then
  sweep_print_header "R18 — paired condition labels: orphan use of OLD names"
  if ((${#RULE_18_OLD_LABELS[@]} == 0)); then
    sweep_print_skipped "RULE_18_OLD_LABELS in config"
  else
    out=$(grep_all_fixed "${RULE_18_OLD_LABELS[@]}")
    if [[ -n "$out" ]]; then sweep_print_findings "$out"; else sweep_print_clean; fi
  fi
fi

# R19 — writing-process archaeology (universal regex + literal extras from config)
if has_check r19; then
  sweep_print_header "R19 — writing-process archaeology"
  pattern='Within-run|Phase~?[0-9]|Attempt~?[0-9]+|\bE0[0-9]\b|originally we used|the most conservative of the candidates|we initially considered|in our first attempt'
  out=$(grep_all "$pattern")
  if ((${#EXTRA_R19_PATTERNS[@]})); then
    extras_out=$(grep_all_fixed "${EXTRA_R19_PATTERNS[@]}")
    [[ -n "$extras_out" ]] && out="${out}${out:+$'\n'}${extras_out}"
  fi
  if [[ -n "$out" ]]; then sweep_print_findings "$out"; else sweep_print_clean; fi
fi

# R20 — load-bearing modifier outside its definition site (config-driven)
if has_check r20; then
  sweep_print_header "R20 — load-bearing scope-tag modifier outside its definition site"
  if [[ -z "$RULE_20_MODIFIER" || -z "$RULE_20_DEFINITION_FILE" ]]; then
    sweep_print_skipped "RULE_20_MODIFIER and RULE_20_DEFINITION_FILE in config"
  else
    out=$(grep -nHE "\\\\emph\\{$RULE_20_MODIFIER|$RULE_20_MODIFIER exploratory|$RULE_20_MODIFIER trace" "${PROSE_FILES[@]}" 2>/dev/null \
           | grep -v "$RULE_20_DEFINITION_FILE" || true)
    if [[ -n "$out" ]]; then sweep_print_findings "$out"; else sweep_print_clean; fi
  fi
fi

# vocab-lock — project-specific vocabulary locks (config-driven, manual-verify)
# Patterns are passed to grep -E as-is (treat as ERE regex); user controls escaping.
if has_check vocab-lock; then
  sweep_print_header "vocab-lock — project-specific vocabulary that should not appear (manually verify; some hits may be legitimate source statements)"
  if ((${#VOCAB_LOCK_PATTERNS[@]} == 0)); then
    sweep_print_skipped "VOCAB_LOCK_PATTERNS in config"
  else
    pattern=""
    for p in "${VOCAB_LOCK_PATTERNS[@]}"; do
      [[ -n "$pattern" ]] && pattern="${pattern}|"
      pattern="${pattern}${p}"
    done
    out=$(grep_all "$pattern")
    if [[ -n "$out" ]]; then sweep_print_findings "$out"; else sweep_print_clean; fi
  fi
fi

# comparator vocabulary lock (universal)
if has_check comparator; then
  sweep_print_header "comparator → baseline (language-phrasebank.md Section J)"
  out=$(grep_all '\bcomparator\b|\bcomparators\b|\bcomparative method\b')
  if [[ -n "$out" ]]; then sweep_print_findings "$out"; else sweep_print_clean; fi
fi

# refs — orphan cross-references (universal)
if has_check refs; then
  sweep_print_header "Orphan \\ref / \\autoref / \\Cref / \\pageref / \\eqref targets"
  mapfile -t LABELS < <(grep -hoE '\\label\{[^}]+\}' "${PROSE_FILES[@]}" "$MAIN_FILE" 2>/dev/null \
                        | sed -E 's/\\label\{([^}]+)\}/\1/' | sort -u)
  orphan_found=0
  while IFS= read -r line; do
    target="${line##*=}"; file="${line%%:*}"
    found=0
    for L in "${LABELS[@]:-}"; do [[ "$L" == "$target" ]] && found=1 && break; done
    if ((!found)); then
      echo "  orphan ref → $target  ($file)"
      orphan_found=1
    fi
  done < <(grep -nHoE '\\(ref|autoref|Cref|pageref|eqref)\{[^}]+\}' "${PROSE_FILES[@]}" "$MAIN_FILE" 2>/dev/null \
           | sed -E 's/(\\(ref|autoref|Cref|pageref|eqref))\{([^}]+)\}/\1=\3/' \
           | awk -F'=' '{print $1"="$NF}')
  ((orphan_found)) && hits=$((hits + 1)) || echo "(clean)"
  echo
fi

# orphan-files — .tex files in sections/ or figures/ NOT \input'd
if has_check orphan-files; then
  sweep_print_header "Orphan .tex files (present but NOT \\input'd by build — likely stale)"
  if ((${#ORPHANS[@]} == 0)); then
    sweep_print_clean
  else
    printf '  %s\n' "${ORPHANS[@]}"
    echo
    hits=$((hits + 1))
  fi
fi

# ----------------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------------
echo "============================================================"
if ((hits == 0)); then
  echo "  All active sweeps clean."
  ((skips > 0)) && echo "  ($skips sweep(s) skipped — supply config to enable.)"
  exit 0
else
  echo "  $hits sweep(s) reported findings — review above."
  ((skips > 0)) && echo "  ($skips sweep(s) skipped — supply config to enable.)"
  ((STRICT)) && exit 1
fi
