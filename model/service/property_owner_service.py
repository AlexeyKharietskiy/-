from model.repository.property_repository import IPropertyRepository, Property, List
from model.domain.user import User


class IPropertyOwnerService:
    def registerProperty(self, property: Property):
        pass

    def viewTenantProfile(self, tenantId: int)-> User:
        pass
    def getUserProperties(self, userId: int)-> List[Property]:
        pass

    def getProperty(self, propertyId: int)-> Property:
        pass

    def deleteProperty(self, propertyId: int):
        pass


class PropertyOwnerService(IPropertyOwnerService):
    def __init__(self, repository: IPropertyRepository):
        self.propertyRepository: IPropertyRepository = repository