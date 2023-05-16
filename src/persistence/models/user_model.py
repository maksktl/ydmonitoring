from sqlalchemy import sql, Column, String, BIGINT

from src.persistence.models.base_models import TimedBaseModel
from src.routers.payload.user_payload import UserPayload


class UserModel(TimedBaseModel):
    __tablename__ = 'users'
    query: sql.Select

    telegram_id = Column(BIGINT, unique=True, index=True)
    telegram_username = Column(String(256), index=True)
    firstname = Column(String(256), nullable=False)
    lastname = Column(String(256))

    def fill(self, payload: UserPayload):
        self.telegram_id = payload.telegram_id
        self.telegram_username = payload.username
        self.firstname = payload.firstname
        self.lastname = payload.lastname
