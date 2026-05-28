from pydantic import BaseModel

class RestaurantCreate(BaseModel):
    name: str
    cuisine: str
    phone_number: str
    address: str


class RestaurantResponse(BaseModel):
    id: int
    name: str
    cuisine: str
    phone_number: str
    address: str
    is_open: bool

    class Config:
        from_attributes = True


class RestaurantUpdate(BaseModel):
    name: str | None = None
    cuisine: str | None = None
    phone_number: str | None = None
    address: str | None = None
    is_open: bool | None = None


class DishCreate(BaseModel):
    name: str
    description: str | None = None
    price: int
    is_available: bool = True
    restaurant_id: int


class DishResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: int
    is_available: bool = True
    restaurant_id: int

    class Config:
        from_attributes = True