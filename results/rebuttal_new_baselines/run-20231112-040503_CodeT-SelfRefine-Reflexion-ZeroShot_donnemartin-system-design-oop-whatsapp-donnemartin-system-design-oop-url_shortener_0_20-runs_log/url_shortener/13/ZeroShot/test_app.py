import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def setup():
	app.DB['users'] = {}
	app.DB['urls'] = {}

@pytest.mark.usefixtures('setup')
def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}

@pytest.mark.usefixtures('setup')
def test_create_url(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/create_url', json={'username': 'test', 'password': 'test', 'original_url': 'https://www.google.com', 'short_url': 'google', 'expiration': (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'URL created successfully'}

@pytest.mark.usefixtures('setup')
def test_redirect_url(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	client.post('/create_url', json={'username': 'test', 'password': 'test', 'original_url': 'https://www.google.com', 'short_url': 'google', 'expiration': (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
	response = client.get('/google')
	assert response.status_code == 302

@pytest.mark.usefixtures('setup')
def test_get_analytics(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	client.post('/create_url', json={'username': 'test', 'password': 'test', 'original_url': 'https://www.google.com', 'short_url': 'google', 'expiration': (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
	client.get('/google')
	response = client.get('/analytics', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'google' in response.get_json()
	assert response.get_json()['google']['clicks'] == 1
