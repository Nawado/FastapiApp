from fastapi import APIRouter

from ..public.v1.exchanges import router as exchanges_v1_router
from ..public.v1.markets import router as markets_v1_router

router = APIRouter(tags=['PUBLIC'])

router.include_router(exchanges_v1_router, tags=['games'], prefix='/v1/exchanges')
router.include_router(markets_v1_router, tags=['games'], prefix='/v1/markets')