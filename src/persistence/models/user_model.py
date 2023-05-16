from sqlalchemy import sql, Column, String, BIGINT

from src.persistence.models.base_models import TimedBaseModel


class UserModel(TimedBaseModel):
    __tablename__ = 'users'
    query: sql.Select

    telegram_id = Column(BIGINT, unique=True, index=True)
    telegram_username = Column(String(256), index=True)
    firstname = Column(String(256), nullable=False)
    lastname = Column(String(256))
