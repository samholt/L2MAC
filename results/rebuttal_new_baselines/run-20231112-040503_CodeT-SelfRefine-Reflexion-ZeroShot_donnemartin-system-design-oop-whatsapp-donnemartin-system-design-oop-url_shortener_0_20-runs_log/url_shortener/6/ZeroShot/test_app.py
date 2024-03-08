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
	assert response.status_code == 201
	assert 'short_url' in response.get_json()

def test_redirect_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

def test_create_user(client):
	response = client.post('/user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User created'

def test_get_user(client):
	client.post('/user', json={'username': 'test', 'password': 'test'})
	response = client.get('/user/test')
	assert response.status_code == 200
	assert response.get_json()['username'] == 'test'

def test_url_expiration(client):
	expiration = (datetime.datetime.now() - datetime.timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:%S')
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'expiration': expiration})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
