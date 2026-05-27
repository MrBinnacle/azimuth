#!/usr/bin/env bash
# AZIMUTH validation gate — enforces the 4 rules in VALIDATION.md (authoritative spec).
# Invoked as a PreToolUse Bash hook with if: "Bash(git commit*)".
# Output: empty stdout (pass) or JSON deny payload (fail).
# If this script diverges from VALIDATION.md, the spec is authoritative — fix this script.

# Consume stdin (hook payload — we don't need anything from it; the `if` filter gates).
read -r _ 2>/dev/null

cd "$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0

FAILS=""

# Check 1: SKILL.md frontmatter description must be exactly 489 chars
if [ -f SKILL.md ]; then
  CHARS=$(awk '/^description: /{flag=1} flag{print; if(/"$/) flag=0}' SKILL.md | tr -d '\n' | wc -c | tr -d ' ')
  if [ "$CHARS" != "489" ]; then
    FAILS="${FAILS}- SKILL.md description is ${CHARS} chars (expected 489)\\n"
  fi
fi

# Check 2: gotchas.md must have exactly 8 numbered sections
if [ -f gotchas.md ]; then
  SECTIONS=$(grep -cE '^## [0-9]+\.' gotchas.md | tr -d ' ')
  if [ "$SECTIONS" != "8" ]; then
    FAILS="${FAILS}- gotchas.md has ${SECTIONS} numbered sections (expected 8)\\n"
  fi
fi

# Check 3: no "precommitment" outside CHANGELOG.md and CLAUDE.md (both document the rule).
# Use git ls-files so only tracked .md files are checked (skips .omc/, install-test copies, etc).
TYPOS=$(git ls-files '*.md' 2>/dev/null | grep -vE '^(CHANGELOG|CLAUDE|VALIDATION)\.md$' | xargs grep -l precommitment 2>/dev/null | head -3 | tr '\n' ' ')
if [ -n "$TYPOS" ]; then
  FAILS="${FAILS}- 'precommitment' typo (use 'pre-commitment') in: ${TYPOS}\\n"
fi

# Check 4: all paths referenced in SKILL.md must exist
if [ -f SKILL.md ]; then
  MISSING=$(grep -oE '(references|diagnostics|templates)/[^ "]+\.md' SKILL.md | sort -u | while read -r f; do [ ! -f "$f" ] && echo "$f"; done | head -5 | tr '\n' ' ')
  if [ -n "$MISSING" ]; then
    FAILS="${FAILS}- Missing paths referenced in SKILL.md: ${MISSING}\\n"
  fi
fi

if [ -n "$FAILS" ]; then
  # Output deny JSON. Newlines in reason use literal \n (already escaped above).
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"AZIMUTH validation gate failed:\\n%s\\nFix and retry commit. Bypass with --no-verify if intentional."}}\n' "$FAILS"
fi
exit 0
