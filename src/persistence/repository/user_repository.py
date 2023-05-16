from typing import Optional

from src.persistence.models.user_model import UserModel


class UserRepository:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = UserRepository()
        return cls._instance

    async def create(self, user: UserModel):
        return await user.create()

    async def update(self, user: UserModel):
        await user.update(
            name=user.name,
            surname=user.surname,
            middle_name=user.middle_name,
            email=user.email,
            telegram_id=user.telegram_id,
            telegram_url=user.telegram_url,
            phone_number=user.phone_number,
            bot_access=user.bot_access,
            admin=user.admin
        ).apply()
        return user

    async def get_by_id(self, id) -> Optional[UserModel]:
        return await UserModel.get(id)

    async def get_by_tg_id_and_deleted_false(self, tg_id):
        result = await UserModel.query.where((UserModel.telegram_id == tg_id) &
                                             (UserModel.deleted == False)).gino.first()
        return result

    async def get_all_by_deleted_false(self, ):
        result = await UserModel.query.where((UserModel.deleted == False)).gino.all()
        return result
