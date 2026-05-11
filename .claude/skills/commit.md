---
description: "Commit changes using conventional commits for semantic versioning. Use when the user says 'commit', 'commit and push', or /commit."
user_invocable: true
---

# Conventional Commit Skill

When committing changes, ALWAYS use the Conventional Commits format so that `python-semantic-release` can automatically determine version bumps.

## Format

```
<type>[optional scope]: <short description>

[optional body with more detail]

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

## Steps

1. Run `git status` and `git diff` to understand all changes.
2. Determine the correct commit type based on the changes:
   - `fix:` — Bug fix (triggers PATCH bump)
   - `feat:` — New feature (triggers MINOR bump)
   - `feat!:` — Breaking change (triggers MAJOR bump)
   - `refactor:` — Code restructuring (no version bump)
   - `chore:` — Maintenance, CI, tooling (no version bump)
   - `test:` — Test changes only (no version bump)
   - `ci:` — CI/CD changes (no version bump)
   - `docs:` — Documentation (no version bump)
3. Write a concise subject line (max 72 chars) describing *what* changed.
4. If the change is non-trivial, add a body explaining *why*.
5. For breaking changes, either use `!` after the type OR add a `BREAKING CHANGE:` footer.
6. Stage specific files (never use `git add .` or `git add -A`).
7. Commit using a HEREDOC for proper formatting.
8. Only push if the user explicitly asked to push.

## Examples

```
fix: convert Decimal to str before JSON serialization in PawaPay
```

```
feat: add reference_id parameter to disbursement and refund

Allows callers to associate disbursements and refunds with external
reference IDs for better traceability.
```

```
feat!: rename service/order_id to reference_type/reference_id

BREAKING CHANGE: PaymentTransaction fields renamed. Run migrations
to apply changes.
```
