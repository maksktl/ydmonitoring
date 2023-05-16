from typing import Optional
from uuid import UUID

from pydantic.main import BaseModel


class UserSchema(BaseModel):
    id: UUID
    telegram_id: int
    telegram_username: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
