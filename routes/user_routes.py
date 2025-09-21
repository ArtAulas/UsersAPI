from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.users_model import UserRequest
from db_config import Base,engine,get_db
from controller.user_controller import UserController

router=APIRouter(prefix='/users')
Base.metadata.create_all(bind=engine)

@router.post('/add')
def insert(request:UserRequest,db:Session=Depends(get_db)):
    return UserController.insert(user=request,db=db)

@router.get('/get')
def select(db:Session=Depends(get_db)):
    return UserController.select(db)