from model.domain.support_request import SupportRequest
from model.infrastructure.DBConext import DBContext


class ISupportRepository:
        def create(self, request: SupportRequest):
            pass

        def read(self, requestId: int)-> SupportRequest:
            pass

        def update(self, request: SupportRequest):
            pass

        def delete(self, requestId: int):
            pass

class SupportRepository(ISupportRepository):
    def __init__(self):
        self.__databaseContext: DBContext