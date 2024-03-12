import pytest
from app import app, URL, urls
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	assert urls[short_url].original == 'https://www.google.com'
	assert urls[short_url].short == short_url
	assert urls[short_url].clicks == 0


def test_redirect_to_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert urls[short_url].clicks == 1


def test_url_expiration(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com', 'expiration': (datetime.now() - timedelta(minutes=1)).isoformat()})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
