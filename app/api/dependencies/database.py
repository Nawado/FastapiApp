from typing import AsyncGenerator, Callable, Type

from aiomysql.connection import Connection
from aiomysql.pool import Pool
from fastapi import Depends
from starlette.requests import Request

from app.db.repos.base import BaseRepository


def _get_db_pool(request: Request) -> Pool:
    return request.app.state.pool


async def _get_connection_from_pool(
        pool: Pool = Depends(_get_db_pool),
) -> AsyncGenerator[Connection, None]:
    async with pool.acquire() as conn:
        yield conn


def get_repository(
        repo_type: Type[BaseRepository],
) -> Callable[[Connection], BaseRepository]:
    def _get_repo(
            conn: Connection = Depends(_get_connection_from_pool),
    ) -> BaseRepository:
        return repo_type(conn)

    return _get_repo
