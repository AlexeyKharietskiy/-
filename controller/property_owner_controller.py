from model.service.property_owner_service import Property, User, List, IPropertyOwnerService
from controller.abstract_controller import Controller


class IPropertyOwnerController:
    def registerProperty(self, proper: Property):
        pass

    def viewTenantProfile(self, tenantId: int)-> User:
        pass

    def getUserProperties(self, userId: int)-> List[Property]:
        pass

    def addProperty(self, proper: Property):
        pass

    def updateProperty(self, proper: Property):
        pass

    def getProperty(self, propertyId: int)-> Property:
        pass

    def deleteProperty(self, propertyId: int):
        pass


class PropertyOwnerController(IPropertyOwnerController, Controller):
    def __init__(self, service: IPropertyOwnerService):
        self.propertyOwnerService: IPropertyOwnerService = service