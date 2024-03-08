import pytest
import app
import time

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register_login(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200


def test_shorten_url(client):
	response = client.post('/register', json={'username': 'test1', 'password': 'test1'})
	assert response.status_code == 200
	response = client.post('/login', json={'username': 'test1', 'password': 'test1'})
	assert response.status_code == 200
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	assert len(short_url) == 6


def test_redirect_url(client):
	response = client.post('/register', json={'username': 'test2', 'password': 'test2'})
	assert response.status_code == 200
	response = client.post('/login', json={'username': 'test2', 'password': 'test2'})
	assert response.status_code == 200
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_analytics(client):
	response = client.post('/register', json={'username': 'test3', 'password': 'test3'})
	assert response.status_code == 200
	response = client.post('/login', json={'username': 'test3', 'password': 'test3'})
	assert response.status_code == 200
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200


def test_admin(client):
	response = client.post('/register', json={'username': 'admin', 'password': 'admin'})
	assert response.status_code == 200
	response = client.post('/login', json={'username': 'admin', 'password': 'admin'})
	assert response.status_code == 200
	response = client.get('/admin')
	assert response.status_code == 200


def test_cache(client):
	response = client.post('/register', json={'username': 'test4', 'password': 'test4'})
	assert response.status_code == 200
	response = client.post('/login', json={'username': 'test4', 'password': 'test4'})
	assert response.status_code == 200
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	start_time = time.time()
	for _ in range(100):
		response = client.get(f'/{short_url}')
		assert response.status_code == 302
	end_time = time.time()
	assert end_time - start_time < 1, 'Cache is not working properly'

