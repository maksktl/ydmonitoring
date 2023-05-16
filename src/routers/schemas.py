from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class UserResult:
    id: UUID
    telegram_id: int
    telegram_username: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]

    def __init__(self, model):
        self.id = model.id
        self.telegram_id = model.telegram_id
        self.telegram_username = model.telegram_username
        self.firstname = model.firstname
        self.lastname = model.lastname
