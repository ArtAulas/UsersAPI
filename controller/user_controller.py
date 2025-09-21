#Controller = Regra de Negócio
from service.user_service import UserService
from models.users_model import UserResponse, UserRequest
from sqlalchemy.orm import Session

class UserController():
    def insert(user:UserRequest,db:Session):
        user_novo=user.model_dump() 
        return UserService.insert(user=user_novo,db=db)

    def select(db:Session):
        users=UserService.select(db)
        return [UserResponse.model_validate(user) for user in users]

    def select_id():
        pass

    def update():
        pass

    def delete():
        pass