from typing import Optional, List

from pydantic import BaseModel

class ExchangeInDB(BaseModel):
    id: int
    name: str
    code: str
    country: str
    currency: str
    countryIso2: str
    countryIso3: str
    tickers: str
