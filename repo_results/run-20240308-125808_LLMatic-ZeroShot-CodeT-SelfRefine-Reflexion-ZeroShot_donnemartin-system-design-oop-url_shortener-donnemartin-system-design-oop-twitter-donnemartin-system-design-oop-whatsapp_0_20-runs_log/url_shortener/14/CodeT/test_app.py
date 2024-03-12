import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_data():
	app.urls = {}
	app.users = {}

@pytest.mark.usefixtures('reset_data')
def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_redirect_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

@pytest.mark.usefixtures('reset_data')
def test_create_user(client):
	response = client.post('/user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert 'message' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_get_user_urls(client):
	client.post('/user', json={'username': 'test', 'password': 'test'})
	client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test'})
	response = client.get('/user/test/urls')
	assert response.status_code == 200
	assert 'urls' in response.get_json()
	assert len(response.get_json()['urls']) == 1
