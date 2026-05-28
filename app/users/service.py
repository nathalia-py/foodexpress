from types import SimpleNamespace
from sqlalchemy.orm import Session
from users import repository
import bcrypt


def create_user(db: Session, user_data):
    hashed_password = bcrypt.hashpw(user_data.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    user_to_save = SimpleNamespace(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_password,
        phone_number=user_data.phone_number
    )

    return repository.save_user(db, user_to_save)

def login_user(db: Session, login_data):
    user = repository.get_user_by_email(db, login_data.email)
    if not user:
        raise ValueError("Invalid email or password")

    if not bcrypt.checkpw(login_data.password.encode("utf-8"), user.hashed_password.encode("utf-8")):
        raise ValueError("Invalid email or password")

    return user

def update_user(db: Session, user_id: int, user_data):
    user = repository.get_user_by_id(db, user_id)
    if not user:
        raise ValueError("User not found")

    if user_data.name is not None:
        user.name = user_data.name
    if user_data.email is not None:
        user.email = user_data.email
    if user_data.password is not None:
        user.hashed_password = bcrypt.hashpw(user_data.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    if user_data.phone_number is not None:
        user.phone_number = user_data.phone_number

    return repository.update_user(db, user)
