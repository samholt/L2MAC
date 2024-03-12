import pytest
from url_shortener import app, urls_db, URL
from datetime import datetime, timedelta

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client

@pytest.fixture(autouse=True)
def clear_db():
	urls_db.clear()

def test_shorten_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 201
	short_url = response.get_json()['short_url']
	assert urls_db[short_url].original_url == 'https://www.google.com'

def test_redirect_to_url(client):
	urls_db['test'] = URL('https://www.google.com', 'test', None)
	response = client.get('/test')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'

def test_redirect_to_expired_url(client):
	urls_db['test'] = URL('https://www.google.com', 'test', datetime.now() - timedelta(days=1))
	response = client.get('/test')
	assert response.status_code == 404
