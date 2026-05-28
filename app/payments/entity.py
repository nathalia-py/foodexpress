from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)

    provider = Column(String, index=True)
    method_type = Column(String, index=True)
    amount = Column(Integer)
    status = Column(String, index=True)
    currency = Column(String, index=True)

    provider_payment_id = Column(String, index=True)
    provider_customer_id = Column(String, index=True)
    provider_payment_method_id = Column(String, index=True)

    card_brand = Column(String, index=True)
    card_last4 = Column(String, index=True)

    pix_qr_code = Column(String, index=True)
    pix_expires_at = Column(DateTime)

    paid_at = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    order = relationship("Order")
    user = relationship("User")

class UserPaymentMethod(Base):
    __tablename__ = "user_payment_methods"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    provider = Column(String, index=True)
    method_type = Column(String, index=True)
    
    provider_customer_id = Column(String, index=True)
    provider_payment_method_id = Column(String, index=True)

    card_brand = Column(String, index=True)
    card_last4 = Column(String, index=True)

    exp_month = Column(Integer)
    exp_year = Column(Integer)

    is_default = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User")
