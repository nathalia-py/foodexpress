from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from orders import service
from orders.schemas import OrderCreate, OrderResponse

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=OrderResponse)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    return service.create_order(db, order_data)