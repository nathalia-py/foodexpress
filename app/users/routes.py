from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from users import service
from users.schemas import UserCreate, UserResponse, UserLogin, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user_data)

@router.post("/login", response_model=UserResponse)
def login_user(login_data: UserLogin, db: Session = Depends(get_db)):
    return service.login_user(db, login_data)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    return service.update_user(db, user_id, user_data)