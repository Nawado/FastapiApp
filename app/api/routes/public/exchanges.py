from fastapi import APIRouter, Depends

from app.api.dependencies.database import get_repository
from app.db.repos.exchanges import ExchangeRepository
from app.models.exchanges.exchanges import ExchangeInDB

router = APIRouter()

@router.get("/{game_id}/", response_model=ExchangeInDB)
async def get_exchange_by_id(
    exchange_id,
    exchange_repo: ExchangeRepository = Depends(get_repository(ExchangeRepository))   
) -> ExchangeInDB:
    _exchange = await exchange_repo.get_exchange_by_id(exchange_id)
    exchange: ExchangeInDB = ExchangeInDB(
        **_exchange.dict()
    )
    return exchange