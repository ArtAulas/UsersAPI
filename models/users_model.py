from pydantic import BaseModel
from db_config import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__='Users'
    id=Column('id',Integer, primary_key=True, autoincrement=True)
    username=Column('username',String(255),nullable=False)
    password=Column('password',String(255),nullable=False)
    cpf=Column('cpf', Integer)

class UserRequest(BaseModel):
    username:str
    password:str
    cpf:int

    class Config:
        from_attributes=True

class UserResponse(BaseModel):
    id:int
    username:str
    password:str
    cpf:int

    class Config:
        from_attributes=True