import pytest
from app import app
from database import users, urls, clicks
from models import User, URL, Click
from datetime import datetime, timedelta


@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'original_url': 'https://www.google.com', 'user_id': 'test_user', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	assert 'shortened_url' in response.get_json()


def test_redirect_to_url(client):
	response = client.post('/shorten', json={'original_url': 'https://www.google.com', 'user_id': 'test_user', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	short_url = response.get_json()['shortened_url']

	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_expired_url(client):
	response = client.post('/shorten', json={'original_url': 'https://www.google.com', 'user_id': 'test_user', 'expiration': (datetime.now() - timedelta(days=1)).isoformat()})
	short_url = response.get_json()['shortened_url']

	response = client.get(f'/{short_url}')
	assert response.status_code == 410
