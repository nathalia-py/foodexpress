from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from delivery import service
from delivery.schemas import DeliveryCreate, DeliveryUpdate, DeliveryResponse

router = APIRouter(prefix="/deliveries", tags=["deliveries"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=DeliveryResponse)
def create_delivery(delivery: DeliveryCreate, db: Session = Depends(get_db)):
    return service.create_delivery(db, delivery)


@router.get("/{delivery_id}", response_model=DeliveryResponse)
def read_delivery(delivery_id: int, db: Session = Depends(get_db)):
    return service.get_delivery(db, delivery_id)