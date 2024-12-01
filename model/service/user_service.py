from model.repository.user_repository import User, IUserRepository
from model.domain.booking import Booking
from typing import List

class IUserService:
        def getUserById(self, userId: int)-> User:
            pass

        def updateUser(self, user: User):
            pass

        def getBookingHistory(self, userId: int)-> List[Booking]:
            pass

        def deleteUser(self, userId: int):
            pass

class UserService(IUserService):
    def __init__(self, repository: IUserRepository):
        self.__bookingRepository: IUserRepository = repository