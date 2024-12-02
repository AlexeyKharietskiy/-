from controller.support_controller import ISupportController


class ISupportView:
    def displaySupportForm(self):
         pass

    def submitSupportRequest(self, request):
         pass

class SupportView(ISupportView):
    pass