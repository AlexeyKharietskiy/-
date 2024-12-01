from controller.abstract_controller import Controller
from model.service.user_service import User, List, Booking, IUserService

class IUserController:
        def getUserProfile(self, userId: int)-> User:
            pass

        def updateProfile(self, user: User):
            pass

        def getBookingHistory(self, userId: int)-> List[Booking]:
            pass

        def deleteUser(self, userId: int):
            pass

class UserController(IUserController, Controller):
    def __init__(self, service: IUserService):
        self.userService: IUserService = service