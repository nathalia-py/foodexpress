from types import SimpleNamespace
from sqlalchemy.orm import Session
from payments import repository

def create_payment(db: Session, payment_data):
    payment_to_save = SimpleNamespace(
        order_id=payment_data.order_id,
        user_id=payment_data.user_id,
        provider=payment_data.provider,
        method_type=payment_data.method_type,
        amount=payment_data.amount,
        status=payment_data.status,
        currency=payment_data.currency,
        provider_payment_id=payment_data.provider_payment_id,
        provider_customer_id=payment_data.provider_customer_id,
        provider_payment_method_id=payment_data.provider_payment_method_id,
        card_brand=payment_data.card_brand,
        card_last4=payment_data.card_last4,
        pix_qr_code=payment_data.pix_qr_code,
        pix_expires_at=payment_data.pix_expires_at,
        paid_at=payment_data.paid_at
    )

    return repository.create_payment(db, payment_to_save)
