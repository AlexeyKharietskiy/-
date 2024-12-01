from model.domain.user import User
from typing import List, Optional


class Property:
    def __init__(self, user: User):
        self.id: int = 0
        self.owner: User = user
        self.location: str
        self.description: str
        self.pricePerNight: float
        self.squareMeters: float
        self.amenities: List[str]
        self.services: List[str]
        self.propertyType: str
        self.allowsPets: bool
        self.photos: List[str]
        self.isSubscriptionPaid: bool