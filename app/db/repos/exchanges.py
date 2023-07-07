from typing import List

from sqlalchemy import select

from app.db.repos.base import BaseRepository
from app.db.tables.exchanges import exchanges_table
from app.models.exchanges.exchanges import ExchangeInDB


class ExchangeRepository(BaseRepository):
        table = exchanges_table

        def get_db_row(self, row) -> ExchangeInDB:
                return ExchangeInDB(**dict(row))
                
        async def get_exchange_by_id(self, id: int) -> ExchangeInDB:
                q = self.table.select().where(exchanges_table.c.id == id)
                row = await self.connection.fetchrow(q)
                if not row:
                        raise Exception("Data not found")
                return self.get_db_row(row)
                
        async def get_exchanges(self, id: int) -> List[ExchangeInDB]:
                q = select(exchanges_table.columns).select_from(exchanges_table)
                row = await self.connection.fetchrow(q)
                if not row:
                        raise Exception("Data not found")
                return [self.get_db_row(row) for row in rows]
