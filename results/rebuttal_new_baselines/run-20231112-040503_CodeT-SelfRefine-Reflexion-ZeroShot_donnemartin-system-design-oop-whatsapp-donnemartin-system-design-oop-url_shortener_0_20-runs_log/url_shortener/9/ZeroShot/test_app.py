import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_data():
	return {'url': 'https://www.google.com', 'user': 'test', 'expires_at': datetime.datetime.now() + datetime.timedelta(days=1)}

@pytest.fixture
def sample_user():
	return {'username': 'test', 'password': 'password'}


def test_shorten_url(client, sample_data):
	response = client.post('/shorten', json=sample_data)
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_url(client, sample_data):
	response = client.post('/shorten', json=sample_data)
	short_url = response.get_json().get('short_url')
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_create_user(client, sample_user):
	response = client.post('/user', json=sample_user)
	assert response.status_code == 201
	assert response.get_json().get('message') == 'User created successfully'


def test_get_user(client, sample_user):
	client.post('/user', json=sample_user)
	response = client.get('/user/test')
	assert response.status_code == 200
	assert response.get_json().get('username') == 'test'
