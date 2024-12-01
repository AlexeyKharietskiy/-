
from model.domain.property import Property
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from model.domain.user import User

class Booking:
    def __init__(self):
        self.id: int
        self.user: 'User'
        self.property: Property
        self.checkIn: str
        self.checkOut: str
        self.numberOfGuests: int
        self.hasPets: bool
        self.paymentStatus: str
