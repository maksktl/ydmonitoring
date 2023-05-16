from typing import Optional

from pydantic.fields import Field
from pydantic.main import BaseModel


class UserPayload(BaseModel):
    telegram_id: int
    username: Optional[str] = Field(max_length=32)
    firstname: Optional[str] = Field(max_length=64)
    lastname: Optional[str] = Field(max_length=64)
