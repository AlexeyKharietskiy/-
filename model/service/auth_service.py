from model.repository.auth_repository import User, IAuthRepository


class IAuthService:
        def register(self, user: User):
            pass

        def login(self, login: str, password: str):
            pass

        def logout(self):
            pass


class AuthService(IAuthService):
    def __init__(self, repository: IAuthRepository):
        self.__authRepository:IAuthRepository = repository