import time
import pytest
from url_shortener import app, urls_db

@pytest.fixture

def client():
	with app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'shortened_url' in response.get_json()


def test_redirect_to_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	shortened_url = response.get_json()['shortened_url']

	response = client.get(f'/{shortened_url}')
	assert response.status_code == 302


def test_url_expiration(client):
	expiration_date = time.time() - 1  # Set the URL to expire immediately
	response = client.post('/shorten_url', json={'url': 'https://www.google.com', 'expiration_date': expiration_date})
	shortened_url = response.get_json()['shortened_url']

	response = client.get(f'/{shortened_url}')
	assert response.status_code == 410
	assert 'error' in response.get_json()


def test_get_analytics(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	shortened_url = response.get_json()['shortened_url']

	# Click the URL
	client.get(f'/{shortened_url}')

	response = client.get(f'/analytics/{shortened_url}')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()
	assert len(response.get_json()['clicks']) == 1
