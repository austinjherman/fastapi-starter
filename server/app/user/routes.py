from typing import List
from app import db
from app.user.crud import index, create, read, read_by_email
from app.user.model import UserReturnScheme, UserCreateScheme
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter


def user_router():

    user_router = APIRouter()

    @user_router.post("/users/", response_model=UserReturnScheme)
    def create_user(user: UserCreateScheme, db: Session = Depends(db.get_db)):
        db_user = read_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(
                status_code=400, detail="Email already registered"
            )
        return create(db=db, user=user)

    @user_router.get("/users/", response_model=List[UserReturnScheme])
    def read_users(
        skip: int = 0, limit: int = 100, db: Session = Depends(db.get_db)
    ):
        users = index(db, skip=skip, limit=limit)
        return users

    @user_router.get("/users/{user_id}", response_model=UserReturnScheme)
    def read_user(user_id: int, db: Session = Depends(db.get_db)):
        db_user = read(db, user_id=user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user

    return user_router
