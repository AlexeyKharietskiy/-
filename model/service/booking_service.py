from model.repository.booking_repository import IBookingRepository
from model.repository.booking_repository import Booking
from model.domain.property import Property
from model.repository.booking_repository import List

class IBookingService:
        def searchProperties(self, criteria)-> List[Property]:
            pass

        def createBooking(self, request)-> Booking:
            pass

        def getCurrentBooking(self, userId: int)-> Booking:
            pass


class BookingService(IBookingService):
    def __init__(self, repository: IBookingRepository):
        self.__bookingRepository: IBookingRepository = repository