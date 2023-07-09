from fastapi import APIRouter, Depends

from typing import List, Dict

from app.api.dependencies.database import get_repository
from app.db.repos.markets import MarketRepository
from app.models.markets.markets import MarketInDB

router = APIRouter()

@router.get("/id/{market_id}/", response_model=MarketInDB)
async def get_market_by_id(
    market_id,
    market_repo: MarketRepository = Depends(get_repository(MarketRepository))   
) -> MarketInDB:
    market = await market_repo.get_market_by_id(market_id)
    return market


@router.get("/", response_model=List[Dict])
async def get_markets(
    market_repo: MarketRepository = Depends(get_repository(MarketRepository))
) -> List[Dict]:
    _market = await market_repo.get_markets()
    markets = []
    for val in _market:
        markets.append(val.dict())
    return markets