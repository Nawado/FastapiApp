import asyncpgsa
from fastapi import FastAPI

from app.core.settings import DATABASE_URL


async def connect_to_db(app: FastAPI) -> None:
    app.state.pool = await asyncpgsa.create_pool(
        str(DATABASE_URL),
        min_size=3,
        max_size=10
    )


async def close_db_connection(app: FastAPI) -> None:
    await app.state.pool.close()
