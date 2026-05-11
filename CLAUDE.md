# Project: kunshort-django-payment

Reusable Django payment app with multiple provider support (PawaPay, Flutterwave, MTN MoMo).

## Commit Convention

This project uses **Conventional Commits** for automatic semantic versioning via `python-semantic-release`.

All commit messages MUST follow this format:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types and their version bumps:

| Type | Version Bump | When to use |
|------|-------------|-------------|
| `fix:` | PATCH (0.0.x) | Bug fixes |
| `feat:` | MINOR (0.x.0) | New features |
| `feat!:` or `BREAKING CHANGE:` footer | MAJOR (x.0.0) | Breaking changes |
| `chore:` | No release | Maintenance, CI, docs |
| `refactor:` | No release | Code restructuring |
| `test:` | No release | Adding/fixing tests |
| `ci:` | No release | CI/CD changes |
| `docs:` | No release | Documentation |

### Examples:

```
fix: convert Decimal to str before JSON serialization in PawaPay
feat: add reference_id parameter to disbursement and refund
feat!: rename service/order_id fields to reference_type/reference_id
chore: update CI workflow
refactor: remove redundant amount type conversions in providers
```

## Build & Test

- `make test` — Run tests
- `make build` — Build package
- `make publish` — Build and publish to PyPI
- `make clean` — Remove build artifacts

## Architecture

- `src/kunshort_payment/service.py` — Main PaymentService singleton
- `src/kunshort_payment/models.py` — PaymentTransaction model with Django signals
- `src/kunshort_payment/providers/` — Provider implementations (pawapay, flutterwave, momo)
- Tests use `pytest` with `pytest-django`
