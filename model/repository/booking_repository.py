from model.domain.booking import Booking
from typing import List
from model.infrastructure.DBConext import DBContext


class IBookingRepository:
        def create(self, booking: Booking):
            pass
        def read(self, bookingId: int)-> Booking:
            pass
        def update(self, booking: Booking):
            pass
        def delete(self, bookingId: int):
            pass
        def findByUserId(self, userId: int)-> List[Booking]:
            pass


class BookingRepository(IBookingRepository):
    def __init__(self):
        self.__databaseContext: DBContext