import pytest
import app
import datetime
import hashlib

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Username already exists'}

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}

def test_shorten(client):
	response = client.post('/shorten', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	assert len(short_url) == 5

	response = client.get(f'/{short_url}')
	assert response.status_code == 302

	response = client.post('/shorten', json={'original_url': 'https://www.google.com', 'username': 'test', 'expiration': (datetime.datetime.now() + datetime.timedelta(seconds=1)).strftime('%Y-%m-%d %H:%M:%S')})
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	assert len(short_url) == 5

	response = client.get(f'/{short_url}')
	assert response.status_code == 302

	response = client.get('/analytics', json={'username': 'test'})
	assert response.status_code == 200
	assert short_url in response.get_json()
	assert response.get_json()[short_url]['clicks'] == 1
