from sqlalchemy.orm import Session
from delivery.entity import Delivery

def create_delivery(db: Session, delivery_data) -> Delivery:
    new_delivery = Delivery(
        order_id=delivery_data.order_id,
        address=delivery_data.address
    )
    db.add(new_delivery)
    db.commit()
    db.refresh(new_delivery)
    return new_delivery

def get_delivery_by_id(db: Session, delivery_id: int) -> Delivery:
    return db.query(Delivery).filter(Delivery.id == delivery_id).first()
