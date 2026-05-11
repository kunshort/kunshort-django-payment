# Changelog

All notable changes to this project will be documented in this file.

## [0.1.6] - 2026-05-11

### Added

- `order_id` field on `PaymentTransaction` model to link transactions to application-specific order identifiers.
- `order_id` parameter to `PaymentService.initiate_payment()`.
- `order_id` is passed through on payment retries via `initiate_payment_retry()`.

## [0.1.5] - Previous release

- Flutterwave provider integration.
- Pawapay provider integration.
- Disbursement and refund support.
