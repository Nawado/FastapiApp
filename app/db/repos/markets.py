from typing import List

from app.db.repos.base import BaseRepository
from app.db.tables.markets import markets_table
from app.models.markets.markets import MarketInDB


class MarketRepository(BaseRepository):
        table = markets_table

        def get_db_row(self, row) -> MarketInDB:
            return MarketInDB(**row)

        async def get_market_by_id(self, id: int) -> MarketInDB:
                q = "SELECT * FROM markets WHERE id = %s;"
                cursor = await self.connection.cursor()
                await cursor.execute(q, (id,))
                
                columns = [desc[0] for desc in cursor.description]
                row = await cursor.fetchone()
                result = dict(zip(columns, row))
                if not row:
                    return None
                return self.get_db_row(result)

        async def get_markets(self) -> List[MarketInDB]:
                q = "SELECT * FROM markets"
                cursor = await self.connection.cursor()
                await cursor.execute(q)
                columns = [desc[0] for desc in cursor.description]
                rows = await cursor.fetchall()
                result = [dict(zip(columns, row)) for row in rows]
                if not rows:
                    return []
                return [self.get_db_row(row) for row in result]