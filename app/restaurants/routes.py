from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from restaurants import service
from restaurants.schemas import RestaurantCreate, RestaurantResponse, RestaurantUpdate, DishCreate, DishResponse

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=RestaurantResponse)
def create_restaurant(restaurant_data: RestaurantCreate, db: Session = Depends(get_db)):
    return service.create_restaurant(db, restaurant_data)

@router.put("/{restaurant_id}", response_model=RestaurantResponse)
def update_restaurant(restaurant_id: int, restaurant_data: RestaurantUpdate, db: Session = Depends(get_db)):
    return service.update_restaurant(db, restaurant_id, restaurant_data)

@router.post("/dishes", response_model=DishResponse)
def create_dish(dish_data: DishCreate, db: Session = Depends(get_db)):
    return service.create_dish(db, dish_data)