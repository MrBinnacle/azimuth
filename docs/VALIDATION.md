# AZIMUTH Validation Spec

Authoritative specification of repo-integrity rules enforced before every commit. Deterministic; no rationale. For the executable enforcement, see `.claude/hooks/validate-azimuth.sh`.

The hook MUST mirror this spec exactly. If the spec and the hook diverge, the spec is authoritative — fix the hook.

## Rules

### Rule 1 — SKILL.md frontmatter description character count

The `description:` field in `SKILL.md` frontmatter MUST be exactly **489 characters**, counting the entire quoted string and stripping newlines.

Reference implementation:
```bash
awk '/^description: /{flag=1} flag{print; if(/"$/) flag=0}' SKILL.md | tr -d '\n' | wc -c
```
Expected output: `489`.

### Rule 2 — gotchas.md section count

`gotchas.md` MUST contain exactly **8** top-level numbered sections matching the regex `^## [0-9]+\.`.

Reference implementation:
```bash
grep -cE '^## [0-9]+\.' gotchas.md
```
Expected output: `8`.

### Rule 3 — Banned token: "precommitment"

The token `precommitment` MUST NOT appear in any git-tracked `.md` file, with three exceptions:

- `CHANGELOG.md` — historical entries may quote the token.
- `docs/VALIDATION.md` — this spec defines the banned token by name.
- `docs/MAINTENANCE.md` — operationally documents the rule alongside the other verification-layer checks.

(`CLAUDE.md` is no longer tracked but is preserved in the hook's exception list defensively in case it ever returns.)

Reference implementation:
```bash
git ls-files '*.md' | grep -vE '^(CHANGELOG|CLAUDE)\.md$|^docs/(VALIDATION|MAINTENANCE)\.md$' | xargs grep -l precommitment
```
Expected output: empty.

### Rule 4 — Path integrity in SKILL.md

Every path matching the regex `(references|diagnostics|domain-policies)/[^ "]+\.md` referenced inside `SKILL.md` MUST exist as a real file at that path.

Reference implementation:
```bash
grep -oE '(references|diagnostics|domain-policies)/[^ "]+\.md' SKILL.md | sort -u | while read -r f; do test -f "$f" || echo "MISSING: $f"; done
```
Expected output: empty.

## Enforcement

`PreToolUse` hook on `Bash` with filter `Bash(git commit*)` invokes `.claude/hooks/validate-azimuth.sh`. The hook returns a deny JSON payload on any failure, naming the failing rule(s) and the offending file(s).

Bypass: `git commit --no-verify` skips the hook. Use only when intentional.

## Independence guarantee

This spec is complete and self-contained. A fork or independent reader can validate AZIMUTH's repo integrity using only this file and the hook script — no other repo artifact is required.
