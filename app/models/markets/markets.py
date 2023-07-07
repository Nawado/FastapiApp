from typing import Optional, List

from pydantic import BaseModel

class MarketInDB(BaseModel):
    id: int
    name: str
    code: str
    country: str
    currency: str
    timezone: Optional[str]
    isopen: bool
	active_tickers: Optional[int]
	update_tickers: Optional[int]