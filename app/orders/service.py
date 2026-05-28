from types import SimpleNamespace
from sqlalchemy.orm import Session
from orders import repository

def create_order(db: Session, order_data):
    order_to_save = SimpleNamespace(
        customer_name=order_data.customer_name,
        customer_address=order_data.customer_address,
        customer_phone_number=order_data.customer_phone_number,
        restaurant_id=order_data.restaurant_id,
        dish_id=order_data.dish_id,
        quantity=order_data.quantity,
        total_price=order_data.total_price
    )

    return repository.save_order(db, order_to_save)
