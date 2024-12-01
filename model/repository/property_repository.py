from model.domain.property import Property
from typing import List
from model.infrastructure.DBConext import DBContext


class IPropertyRepository:
        def create(self, proper: Property):
            pass

        def read(self, propertyId: int)-> Property:
            pass

        def update(self, proper: Property):
            pass

        def delete(self, propertyId: int):
            pass

        def search(self, criteria: str)-> List[Property]:
            pass

        def findByUserId(self, userId: int)-> List[Property]:
            pass

class PropertyRepository(IPropertyRepository):
    def __init__(self):
        self.__databaseContext: DBContext