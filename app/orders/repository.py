from sqlalchemy.orm import Session
from orders.entity import Order

def save_order(db: Session, order_data) -> Order:
    new_order = Order(
        customer_name=order_data.customer_name,
        customer_address=order_data.customer_address,
        customer_phone_number=order_data.customer_phone_number,
        restaurant_id=order_data.restaurant_id,
        dish_id=order_data.dish_id,
        quantity=order_data.quantity,
        total_price=order_data.total_price
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order
