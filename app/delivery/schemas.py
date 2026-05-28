from pydantic import BaseModel

class DeliveryCreate(BaseModel):
    order_id: int
    address: str


class DeliveryUpdate(BaseModel):
    address: str | None = None
    status: str | None = None


class DeliveryResponse(BaseModel):
    id: int
    order_id: int
    address: str
    status: str

    class Config:
        from_attributes = True
