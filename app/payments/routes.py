from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from payments import service
from payments.schemas import PaymentCreate, PaymentResponse

router = APIRouter(prefix="/payments", tags=["Payments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=PaymentResponse)
def create_payment(payment_data: PaymentCreate, db: Session = Depends(get_db)):
    return service.create_payment(db, payment_data)