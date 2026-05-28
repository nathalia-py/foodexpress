from sqlalchemy.orm import Session
from users.entity import User

def save_user(db: Session, user_data) -> User:
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=user_data.hashed_password,
        phone_number=user_data.phone_number
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user: User) -> User:
    db.commit()
    db.refresh(user)
    return user