# Changelog

All notable changes to this project will be documented in this file.

## [0.2.1] - 2026-05-11

### Added

- `reference_id` parameter to `initiate_disbursement()` and `initiate_refund()`.
- Makefile with `test`, `build`, `publish`, and `clean` targets.

## [0.2.0] - 2026-05-11

### Changed (BREAKING)

- Renamed `PaymentTransaction.service` to `reference_type`.
- Renamed `PaymentTransaction.order_id` to `reference_id`.
- Renamed `service` parameter to `reference_type` in `initiate_payment()`, `initiate_disbursement()`, and signal kwargs.
- Renamed `order_id` parameter to `reference_id` in `initiate_payment()`.
- `initiate_payment_retry()` now passes `reference_type` and `reference_id`.

### Migration

- Run `python manage.py migrate` to apply the field renames (`0003`, `0004`).

## [0.1.6] - 2026-05-11

### Added

- `order_id` field on `PaymentTransaction` model.
- `order_id` parameter to `PaymentService.initiate_payment()`.

## [0.1.5] - Previous release

- Flutterwave provider integration.
- Pawapay provider integration.
- Disbursement and refund support.
