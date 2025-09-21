#Service = Query com o banco de dados
from sqlalchemy.orm import Session
from models.users_model import User

class UserService():
    def insert(user,db:Session):
        db.add(User(**user))
        return user

    def select(db:Session):
        return db.query(User).all()

    def select_id():
        pass

    def update():
        pass

    def delete():
        pass