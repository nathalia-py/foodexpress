from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    customer_address = Column(String, nullable=False)
    customer_phone_number = Column(String, nullable=False)

    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    dish_id = Column(Integer, ForeignKey("dishes.id"), nullable=False)

    quantity = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)

    status = Column(String, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    restaurant = relationship("Restaurant")
    dish = relationship("Dish")
