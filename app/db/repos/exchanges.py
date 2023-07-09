from typing import List

from app.db.repos.base import BaseRepository
from app.db.tables.exchanges import exchanges_table
from app.models.exchanges.exchanges import ExchangeInDB


class ExchangeRepository(BaseRepository):
        table = exchanges_table

        def get_db_row(self, row) -> ExchangeInDB:
                return ExchangeInDB(**row)

        async def get_exchange_by_id(self, id: int) -> ExchangeInDB:
                q = "SELECT * FROM exchanges WHERE id = %s;"
                cursor = await self.connection.cursor()
                await cursor.execute(q, (id,))
                
                columns = [desc[0] for desc in cursor.description]
                row = await cursor.fetchone()
                result = dict(zip(columns, row))
                if not row:
                        return None
                return self.get_db_row(result)

        async def get_exchanges(self) -> List[ExchangeInDB]:
                q = "SELECT * FROM exchanges"
                cursor = await self.connection.cursor()
                await cursor.execute(q)
                columns = [desc[0] for desc in cursor.description]
                rows = await cursor.fetchall()
                result = [dict(zip(columns, row)) for row in rows]
                if not rows:
                        return []
                return [self.get_db_row(row) for row in result]