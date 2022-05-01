
from random import choice
import string
from fastapi import Depends
from src.shortener.repositories import ShorterRepo, get_shortener_repo


def get_shortener_service(repository: ShorterRepo = Depends(get_shortener_repo)):
    try:
        service = ShorterService(repository)
        yield service
    finally:
        pass


class ShorterService():
    def __init__(self, repository: ShorterRepo):
        self.repository = repository
        
        
    def shortcode(self):
        """method to generate shortcode"""
        return ''.join(choice(string.ascii_letters+string.digits) for _ in range(8))
    
    
    def create_shorter(self,url: str):
        """method to shorter url"""
        item = self.repository.find_by_url(url=url)
        if item:
            return item.shortcode
        else:
            shortcode = self.shortcode()
            """while not exist shortcode in db generate another"""
            while self.repository.find_by_shortcode(shortcode=shortcode) != None:
                shortcode = self.shortcode()
            
            new_shorter = self.repository.create({"url":url, "shortcode": shortcode})
            return new_shorter.shortcode


    def get_expand(self, shortcode: str):
        """method to get url by shortcode"""
        item = self.repository.find_by_shortcode(shortcode=shortcode)
        if item:
            return item.url
        else:   
            return None