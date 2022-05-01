from pydantic import AnyUrl, BaseModel


class ShortenerRequest(BaseModel):
    url: AnyUrl
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "url": "https://www.google.com"
            }
        }
    
class ShorterResponse(BaseModel):
    shortcode: str
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "shortcode": "RZ9RgHxz"
            }
        }
    
class ExpanderResponse(BaseModel):
    url: AnyUrl
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "url": "https://www.google.com"
            }
        }