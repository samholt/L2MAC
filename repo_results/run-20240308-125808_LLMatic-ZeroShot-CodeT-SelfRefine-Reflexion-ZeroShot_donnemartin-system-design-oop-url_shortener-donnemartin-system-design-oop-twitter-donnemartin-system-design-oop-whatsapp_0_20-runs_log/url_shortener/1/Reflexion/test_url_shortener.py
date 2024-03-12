import pytest
import url_shortener
from url_shortener import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	assert 'original_url' in response.get_json()
	assert 'clicks' in response.get_json()


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'message' in response.get_json()


def test_login(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'message' in response.get_json()
