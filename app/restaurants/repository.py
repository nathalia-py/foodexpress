from sqlalchemy.orm import Session
from restaurants.entity import Restaurant
from restaurants.entity import Dish

def save_restaurant(db: Session, restaurant_data) -> Restaurant:
    new_restaurant = Restaurant(
        name=restaurant_data.name, 
        cuisine=restaurant_data.cuisine, 
        phone_number=restaurant_data.phone_number, 
        address=restaurant_data.address)
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    return new_restaurant

def save_dish(db: Session, dish_data) -> Dish:
    new_dish = Dish(
        name=dish_data.name, 
        description=dish_data.description, 
        price=dish_data.price, 
        restaurant_id=dish_data.restaurant_id)
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return new_dish

def get_restaurant_by_id(db: Session, restaurant_id: int) -> Restaurant:
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

def update_restaurant(db: Session, restaurant: Restaurant) -> Restaurant:
    db.commit()
    db.refresh(restaurant)
    return restaurant
