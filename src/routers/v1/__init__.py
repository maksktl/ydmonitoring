from fastapi import APIRouter

from src.routers.v1.user_route import router as user_router

v1_router = APIRouter(
    prefix='/v1'
)

v1_router.include_router(user_router)
