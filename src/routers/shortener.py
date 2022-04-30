from fastapi import APIRouter

router = APIRouter(
    prefix="/shortener",
    tags=["Shortener"],
    responses={404: {"description": "Not found"}},
)

@router.get('/')
def index():
    return {''}