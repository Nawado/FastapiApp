import aiomysql
from fastapi import FastAPI

from app.core.settings import MY_SQL_SERVER, MY_SQL_DB, MY_SQL_PORT, MY_SQL_USER, MY_SQL_PASSWORD


async def connect_to_db(app: FastAPI) -> None:
    app.state.pool = await aiomysql.create_pool(
        host=str(MY_SQL_SERVER),
        port=int(MY_SQL_PORT),
        user=str(MY_SQL_USER),
        password=str(MY_SQL_PASSWORD),
        db=str(MY_SQL_DB),
        minsize=3,
        maxsize=10
    )


async def close_db_connection(app: FastAPI) -> None:
    await app.state.pool.close()
