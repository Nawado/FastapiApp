from fastapi import APIRouter, Depends

from typing import List, Dict

from app.api.dependencies.database import get_repository
from app.db.repos.exchanges import ExchangeRepository
from app.models.exchanges.exchanges import ExchangeInDB

router = APIRouter()

@router.get("/id/{exchange_id}/", response_model=ExchangeInDB)
async def get_exchange_by_id(
    exchange_id,
    exchange_repo: ExchangeRepository = Depends(get_repository(ExchangeRepository))   
) -> ExchangeInDB:
    exchange = await exchange_repo.get_exchange_by_id(exchange_id)
    return exchange


@router.get("/", response_model=List[Dict])
async def get_exchanges(
    exchange_repo: ExchangeRepository = Depends(get_repository(ExchangeRepository))
) -> List[Dict]:
    _exchange = await exchange_repo.get_exchanges()
    exchanges = []
    for val in _exchange:
        exchanges.append(val.dict())
    return exchanges