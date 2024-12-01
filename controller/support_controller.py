from model.service.support_service import SupportRequest, ISupportService
from controller.abstract_controller import Controller


class ISupportController:
    def sendSupportRequest(self, request: SupportRequest):
        pass


class SupportController(ISupportController, Controller):
    def __init__(self, service: ISupportService):
        self.supportService: ISupportService = service
