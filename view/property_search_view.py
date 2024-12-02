from controller.property_owner_controller import IPropertyOwnerController


class IPropertySearchView:
    def displaySearchResults(self, properties):
         pass

    def displayPropertyDetails(self, proper):
         pass

class PropertySearchView(IPropertySearchView):
    pass