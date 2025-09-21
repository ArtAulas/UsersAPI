from models.users_model import *
from sqlalchemy.orm import Session

class UserRepository():
    def insert(user:UserRequest,db:Session):
        user_novo=user.model_dump() #tranforma o objeto em dicionário
        db.add(User(**user_novo)) #User(**user_novo) traduz as chaves do dicionário como atributos da classe
        db.commit()
        return user_novo

    def select(db:Session):
        users=db.query(User).all()
        return [UserResponse.model_validate(user) for user in users]
    
    def select_id(id:int,db:Session):
        user=db.query(User).filter(User.id==id).first()
        return user

    def update(id:int,user:UserRequest,db:Session):
        db.merge(User(id=id,**user.model_dump()))
        db.commit()
        user_novo=UserRepository.select_id(id,db)
        return user_novo

    def delete(id:int,db:Session):
        user=UserRepository.select_id(id,db)
        db.delete(user)
        db.commit()