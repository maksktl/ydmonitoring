import logging

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from src.config import Config
from src.persistence.database import Database
from src.routers.v1.user_route import router as user_router

logging.basicConfig(
    level=logging.INFO,
    format=u'%(levelname)-8s %(name)s:%(lineno)d [%(asctime)s] - %(message)s',
    # filename='back.log'
)

# Application initialization
app = FastAPI(
    title="Last seen VPN backend service",
    description="This is a backend service for the last seen VPN service",
    version="0.1.0",
    docs_url="/",
    redoc_url=None,
    openapi_url="/openapi.json",
    openapi_tags=[
        {
            "name": "vpn",
            "description": "vpn related operations"
        },
        {
            "name": "users",
            "description": "User related operations"
        }
    ]
)
database = Database.get_instance()
config = Config.get_instance('.env')

# Register routers
app.include_router(user_router)


# TODO: add routers for other entities


@app.on_event("startup")
async def startup():
    #  Initialize cache
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

    #   Connect to database
    await database.setup(
        f'postgresql+asyncpg://{config.db.user}:{config.db.password}@{config.db.host}/{config.db.database}?client_encoding=utf8')
