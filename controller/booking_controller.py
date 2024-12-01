from controller.abstract_controller import Controller
from model.service.booking_service import Property, Booking, List, IBookingService

class IBookingController:
        def searchProperties(self, criteria)-> List[Property]:
            pass

        def createBooking(self, request)-> Booking:
            pass

        def getCurrentBooking(self, userId: int)-> Booking:
            pass


class BookingController(IBookingController, Controller):
    def __init__(self, service: IBookingService):
        self.__bookingService: IBookingService = service