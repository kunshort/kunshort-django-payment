from django.urls import path

from kunshort_payment.admin import PaymentTransactionAdmin
from kunshort_payment.views import (
    update_flutterwave_transaction,
    update_pawapay_transaction,
    update_momo_omo_transaction,
    update_momo_disbursement_transaction,
    check_transaction_status,
    retry_failed_transaction
)

urlpatterns = [
    path("flutterwave/webhook/", update_flutterwave_transaction, name="flutterwave-webhook"),
    path("pawapay/webhook/", update_pawapay_transaction, name="pawapay-webhook"),
    path("momo/collection/webhook/", update_momo_omo_transaction, name="momo-collection-webhook"),
    path("momo/disbursement/webhook/", update_momo_disbursement_transaction, name="momo-disbursement-webhook"),
    path('check_transaction_status/<str:transaction_id>/', check_transaction_status, name='check_transaction_status'),
    path('retry-failed-transaction/<str:transaction_id>/<str:external_reference>/', PaymentTransactionAdmin.retry_failed_transaction, name="retry_failed_transaction"),
    path('initiate_refund/<str:transaction_id>/<str:external_reference>/', PaymentTransactionAdmin.initiate_refund, name="initiate_refund"),
    path('retry-payment/<str:transaction_id>/', retry_failed_transaction, name='user-retry-failed-transaction')
]
