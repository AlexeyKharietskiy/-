from model.service.auth_service import User, IAuthService
from controller.abstract_controller import Controller


class IAuthController:
        def register(self, user: User):
            pass

        def login(self, login: str, password: str):
            pass

        def logout(self):
            pass

class AuthController(IAuthController, Controller):
    def __init__(self, service: IAuthService):
        self.authService: IAuthService = service