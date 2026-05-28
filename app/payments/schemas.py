from datetime import datetime
from pydantic import BaseModel

class PaymentCreate(BaseModel):
    order_id: int
    user_id: int
    provider: str
    method_type: str
    amount: int
    status: str = "pending"
    currency: str = "BRL"
    provider_payment_id: str | None = None
    provider_customer_id: str | None = None
    provider_payment_method_id: str | None = None
    card_brand: str | None = None
    card_last4: str | None = None
    pix_qr_code: str | None = None
    pix_expires_at: datetime | None = None
    paid_at: datetime | None = None

class PaymentResponse(PaymentCreate):
    id: int

    class Config:
        from_attributes = True
