from fastapi import APIRouter

from ..public.v1.exchanges import router as exchanges_v1_router

router = APIRouter(tags=['PUBLIC'])

router.include_router(exchanges_v1_router, tags=['games'], prefix='/v1/exchanges')