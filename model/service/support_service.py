from model.repository.support_repository import SupportRequest, ISupportRepository


class ISupportService:
    def sendSupportRequest(self, request: SupportRequest):
        pass


class SupportService(ISupportService):
    def __init__(self, repository: ISupportRepository):
        self.supportRepository: ISupportRepository = repository