from types import SimpleNamespace
from sqlalchemy.orm import Session
from restaurants import repository

def create_restaurant(db: Session, restaurant_data):
    restaurant_to_save = SimpleNamespace(
        name=restaurant_data.name,
        address=restaurant_data.address,
        cuisine=restaurant_data.cuisine,
        phone_number=restaurant_data.phone_number
    )

    return repository.save_restaurant(db, restaurant_to_save)

def update_restaurant(db: Session, restaurant_id: int, restaurant_data):
    restaurant = repository.get_restaurant_by_id(db, restaurant_id)
    if not restaurant:
        raise ValueError("Restaurant not found")

    if restaurant_data.name is not None:
        restaurant.name = restaurant_data.name
    if restaurant_data.address is not None:
        restaurant.address = restaurant_data.address
    if restaurant_data.phone_number is not None:
        restaurant.phone_number = restaurant_data.phone_number

    return repository.update_restaurant(db, restaurant)

def create_dish(db: Session, dish_data):
    dish_to_save = SimpleNamespace(
        name=dish_data.name,
        description=dish_data.description,
        price=dish_data.price,
        restaurant_id=dish_data.restaurant_id
    )

    return repository.save_dish(db, dish_to_save)