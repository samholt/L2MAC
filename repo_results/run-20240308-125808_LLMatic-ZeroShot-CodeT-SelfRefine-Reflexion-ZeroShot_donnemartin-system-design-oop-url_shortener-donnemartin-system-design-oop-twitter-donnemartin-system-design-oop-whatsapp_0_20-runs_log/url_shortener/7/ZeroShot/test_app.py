import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

def test_redirect_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

def test_create_user(client):
	response = client.post('/user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201

def test_get_user(client):
	client.post('/user', json={'username': 'test', 'password': 'test'})
	response = client.get('/user/test')
	assert response.status_code == 200
	assert 'username' in response.get_json()
	assert 'urls' in response.get_json()

def test_url_expiration(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'expires_at': datetime.datetime.now() - datetime.timedelta(days=1)})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
