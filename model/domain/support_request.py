from model.domain.user import User


class SupportRequest:
    def __init__(self, user: User):
        self.id: int = 0
        self.user: User = user
        self.issueType: str
        self.issueDescription: str
        self.requestDate: str
