from fastapi import APIRouter

from src.routers.shortener import sub_router as shortener_router

router = APIRouter()
router.include_router(shortener_router)


__all__ = ["router"]