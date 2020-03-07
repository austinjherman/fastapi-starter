from app import db
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)

    def __str__(self):
        return 'User(id='+self.id+', email='+self.email+', name='+self.name+')'

    def __repr__(self):
        return (
            '{'
            'id: ' + str(self.id) + ', '
            'email: ' + self.email + ', '
            'name: ' + self.name +
            '}'
        )


class UserBaseScheme(BaseModel):
    email: str
    name: str


class UserReturnScheme(UserBaseScheme):
    id: int

    class Config:
        orm_mode = True


class UserCreateScheme(UserBaseScheme):
    password: str
