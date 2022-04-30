from fastapi.testclient import TestClient


def test_shortener_bad_method(client: TestClient):
    response = client.get('shortener')
    assert response.status_code == 405
    
    
def test_expander_bad_method(client: TestClient):
    response = client.post('expander')
    assert response.status_code == 405
    
    
def test_shortener_in_db(client: TestClient):
    response = client.post(
        url="shortener",
        headers={"Content-Type": "application/json"},
        json={"url": "www.google.com"}
    )
    assert response.json()['shortcode'] == '6VcwJUYK'
    
    
def test_expander_in_db(client: TestClient):
    response = client.get(
        url="expander",
        params={"shortcode": "6VcwJUYK"}
    )
    assert response.json()['url'] == 'www.google.com'
    
    
def test_shortener_bad_request(client: TestClient):
    response = client.post(
        url="shortener",
        headers={"Content-Type": "application/json"},
        json={"url": "malurl"}
    )
    assert response.status_code == 422
    
    
def test_expander_bad_request(client: TestClient):
    response = client.get(
        url="expander",
        params={}
    )
    assert response.status_code == 422
    
    
def test_expander_not_found(client: TestClient):
    response = client.get(
        url="expander",
        params={"shortcode": "8KciCwlF"}
    )
    assert response.status_code == 404
    
    
def test_shortener(client: TestClient):
    response = client.post(
        url="shortener",
        headers={"Content-Type": "application/json"},
        json={"url": "www.github.com"}
    )
    assert len(response.json()['shortcode']) == 8
    

def test_shortener_and_expander(client: TestClient):
    url = "www.facebook.com"
    response = client.post(
        url="shortener",
        headers={"Content-Type": "application/json"},
        json={"url": url}
    )
    shortcode = response.json()['shortcode']
    assert  len(shortcode) == 8
    
    response = client.get(
        url="expander",
        params={"shortcode": shortcode}
    )
    assert response.json()['url'] == url
