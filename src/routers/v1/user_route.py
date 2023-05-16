from uuid import UUID

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.routers.payload.user_payload import UserPayload
from src.services.user_service import UserService

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users']
)
user_service = UserService.get_instance()


# TODO: Add validations for user by pydentic

@router.get('/')
@cache(expire=60)
async def get_users():
    return await user_service.get_users()


@router.get('/{user_id}')
@cache(expire=60)
async def get_user(user_id: UUID):
    return await user_service.get_user(user_id)


@router.post('/')
async def create_user(payload: UserPayload):
    return await user_service.create_user(payload)


@router.put('/{user_id}')
async def update_user(user_id: UUID, payload: UserPayload):
    return await user_service.update_user(payload, user_id)


@router.delete('/{user_id}')
async def delete_user(user_id: UUID):
    return await user_service.delete_user(user_id)
