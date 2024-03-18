import pytest
import app
import requests

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'message' in response.get_json()

	# Test duplicate username
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert 'error' in response.get_json()


def test_login(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'urls' in response.get_json()


def test_shorten_url(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/shorten', json={'username': 'test', 'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'shortened_url' in response.get_json()

	# Test unauthenticated user
	response = client.post('/shorten', json={'username': 'unauthenticated', 'url': 'https://www.google.com'})
	assert response.status_code == 401
	assert 'error' in response.get_json()


def test_redirect_url(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/shorten', json={'username': 'test', 'url': 'https://www.google.com'})
	short_url = response.get_json()['shortened_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'


def test_invalid_url(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/shorten', json={'username': 'test', 'url': 'invalid_url'})
	assert response.status_code == 400
	assert 'error' in response.get_json()


def test_url_not_found(client):
	response = client.get('/nonexistent')
	assert response.status_code == 404
	assert 'error' in response.get_json()
