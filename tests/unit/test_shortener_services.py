
from src.shortener.repositories import ShorterRepo
from src.shortener.services import ShorterService


def test_shorter_in_db(shorturl, service: ShorterService):
    assert service.create_shorter('http://www.google.com') == '6VcwJUYK'


def test_shorter(shorturl, service: ShorterService):
    assert len(service.create_shorter('www.github.com')) == 8
    

def test_shortcode(service: ShorterService):
    assert len(service.shortcode()) == 8
    
        
def test_expand_in_db(shorturl, service: ShorterService):
    assert service.get_expand('6VcwJUYK') == 'http://www.google.com'
    

def test_get_by_shortcode(shorturl, repository: ShorterRepo):
    assert repository.find_by_shortcode('6VcwJUYK').url == 'http://www.google.com'
    
    
def test_get_by_url(shorturl, repository: ShorterRepo):
    assert repository.find_by_url('http://www.google.com').shortcode == '6VcwJUYK'
    
    
def test_expand_not_exist(service: ShorterService):
    assert service.get_expand('8KciCwlF') == None
    
