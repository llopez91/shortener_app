from src.shortener.services import shorter, expand


def test_shorter_in_db(application):
    assert shorter('www.google.com') == '6VcwJUYK'
    
def test_shorter(application):
    assert len(shorter('www.github.com')) == 8
        
def test_expand_in_db(application):
    assert expand('6VcwJUYK') == 'www.google.com'
    
def test_expand_not_exist(application):
    assert expand('8KciCwlF') == None
    
