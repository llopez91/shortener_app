from fastapi import Depends
from sqlalchemy.orm import Session
from src.core.db.session import get_db
from src.shortener.models import ShortUrl



def get_shortener_repo(session: Session = Depends(get_db)):
    try:
        repo = ShorterRepo(db=session)
        yield repo
    finally:
        session.close()


class ShorterRepo():
    def __init__(self, db: Session):
        self.db = db
        self.model = ShortUrl
        
    def all(self):
        return self.db.query(self.model).all()

    def find(self, id: int):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, attributes: dict):
        item = self.model(**attributes)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item
    
    def find_by_shortcode(self, shortcode):
        return self.db.query(self.model).filter_by(shortcode=shortcode).first()
    
    def find_by_url(self, url):
        return self.db.query(self.model).filter_by(url=url).first()
