from fastapi import APIRouter, Depends, status
from src.shortener.schemas import ShortenerRequest, ShorterResponse, ExpanderResponse
from src.core.exceptions.base import NotFoundException
from src.shortener.services import ShorterService, get_shortener_service

sub_router = APIRouter(
    prefix="",
    tags=["Shortener"],
    responses={404: {"description": "Not found"}},
)

@sub_router.post('/shortener', response_model=ShorterResponse, status_code=status.HTTP_201_CREATED)
def create_shortener(request: ShortenerRequest, service: ShorterService = Depends(get_shortener_service)):
    return {'shortcode':service.create_shorter(request.url)}

@sub_router.get('/expander', response_model=ExpanderResponse)
def create_shortener(shortcode:str, service: ShorterService = Depends(get_shortener_service)):
    url = service.get_expand(shortcode)
    if not url:
        raise NotFoundException(message="Resource Not Found") 
    else:
        return {'url': url}