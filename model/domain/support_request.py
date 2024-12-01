from model.domain.user import User


class SupportRequest:
    def __init__(self):
        self.id: int
        self.user: User
        self.issueType: str
        self.issueDescription: str
        self.requestDate: str
