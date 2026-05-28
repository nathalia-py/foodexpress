from types import SimpleNamespace
from sqlalchemy.orm import Session
from delivery import repository

def create_delivery(db: Session, delivery_data):
    delivery_to_save = SimpleNamespace(
        order_id=delivery_data.order_id,
        address=delivery_data.address
    )

    return repository.create_delivery(db, delivery_to_save)

def get_delivery(db: Session, delivery_id: int):
    return repository.get_delivery_by_id(db, delivery_id)
