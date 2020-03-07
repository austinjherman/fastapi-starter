import bcrypt
from sqlalchemy.orm import Session
from app.user.model import User as UserModel, UserCreateScheme


# index
def index(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


# create
def create(db: Session, user: UserCreateScheme):
    hashed_password = bcrypt.hashpw(
        user.password.encode('utf8'), bcrypt.gensalt(14)
    )
    db_user = UserModel(
        email=user.email, password=hashed_password, name=user.name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# read
def read(db: Session, user_id: int):
    return db.query(
        UserModel
    ).filter(UserModel.id == user_id).first()


def read_by_email(db: Session, email: str):
    return db.query(
        UserModel
    ).filter(UserModel.email == email).first()
