from dataclasses import dataclass
from uuid import UUID


@dataclass
class UserFullDto:
    id: UUID
    telegram_id: int
    telegram_username: str
    firstname: str
    lastname: str

    def __init__(self, model):
        self.id = model.id
        self.telegram_id = model.telegram_id
        self.telegram_username = model.telegram_username
        self.firstname = model.firstname
        self.lastname = model.lastname
