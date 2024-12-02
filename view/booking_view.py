from controller.booking_controller import IBookingController


class IBookingView:
    def displayBookingConfirmation(self, booking):
         pass

    def displayCurrentBooking(self):
         pass

class BookingView(IBookingView):
    pass