from model.domain.user import User
from model.infrastructure.DBConext import DBContext

class IUserRepository:
        def create(self, user: User):
            pass

        def read(self, userId: int)-> User:
            pass

        def update(self, user: User):
            pass

        def delete(self, userId: int):
            pass


class UserRepository(IUserRepository):
    def __init__(self):
        self.__databaseContext: DBContext
