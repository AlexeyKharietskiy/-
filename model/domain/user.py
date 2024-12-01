from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from model.domain.booking import Booking

class User:
    def __init__(self):
        self.id: int = 0
        self.name: str = ''
        self.login: str = ''
        self.password: str = ''
        self.gender: str = ''
        self.birthDate: str= ''
        self.country: str= ''
        self.contactInfo: str = ''
        self.profilePicture: str = ''
        self.bookingHistory: List['Booking'] = []


