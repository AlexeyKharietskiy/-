from controller.user_controller import IUserController


class IUserView:
    def displayProfile(self):
         pass

    def displayBookingHistory(self, bookings):
         pass

    def displayOwnedProperties(self, properties):
         pass

    def displayAddPropertyForm(self):
         pass

    def displayUserForm(self, user):
         pass

    def goToSupportPage(self):
         pass

class UserView(IUserView):
    pass