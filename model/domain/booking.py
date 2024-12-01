from model.domain.property import Property
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from model.domain.user import User

class Booking:
    def __init__(self, user: 'User', proper: Property):
        self.id: int = 0
        self.user: 'User' = user
        self.property: Property = proper
        self.checkIn: str
        self.checkOut: str
        self.numberOfGuests: int
        self.hasPets: bool
        self.paymentStatus: str
