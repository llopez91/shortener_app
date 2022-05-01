from src.core.db.session import Base
from sqlalchemy import Column, DateTime, Integer, String
from datetime import datetime

class ShortUrl(Base):
    __tablename__ = 'short_urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(500), nullable=False)
    shortcode = Column(String(20), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)
    
    def __repr__(self):
        return '<ShortUrl %s: %s>' % (self.url, self.shortcode)