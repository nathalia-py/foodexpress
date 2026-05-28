from pydantic import BaseModel

class OrderCreate(BaseModel):
    customer_name: str
    customer_address: str
    customer_phone_number: str
    restaurant_id: int
    dish_id: int
    quantity: int
    total_price: int

class OrderResponse(BaseModel):
    id: int
    customer_name: str
    customer_address: str
    customer_phone_number: str
    restaurant_id: int
    dish_id: int
    quantity: int
    total_price: int
    status: str

    class Config:
        from_attributes = True
