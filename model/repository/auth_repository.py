from model.domain.user import User
from model.infrastructure.DBConext import DBContext


class IAuthRepository:
        def create(self, user: User):
            pass

        def readByLogin(self, login: str):
            pass

        def update(self, user: User):
            pass

        def delete(self, userId: int):
            pass


class AuthRepository(IAuthRepository):
    def __init__(self):
        self.__databaseContext: DBContext