import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('url, user, expires_at', [
	('http://example.com', 'testuser', datetime.datetime.now() + datetime.timedelta(days=1)),
	('http://google.com', 'testuser', datetime.datetime.now() + datetime.timedelta(days=1))
])
def test_shorten_url(client, url, user, expires_at):
	response = client.post('/shorten', json={'url': url, 'user': user, 'expires_at': expires_at})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()

@pytest.mark.parametrize('username, password', [
	('testuser', 'password'),
	('admin', 'admin')
])
def test_create_user(client, username, password):
	response = client.post('/user', json={'username': username, 'password': password})
	assert response.status_code == 201
	assert 'message' in response.get_json()

@pytest.mark.parametrize('username', [
	('testuser'),
	('admin')
])
def test_get_user(client, username):
	response = client.get(f'/user/{username}')
	assert response.status_code == 200
	assert 'username' in response.get_json()
	assert 'urls' in response.get_json()

@pytest.mark.parametrize('username, password', [
	('testuser', 'password'),
	('admin', 'admin')
])
def test_login(client, username, password):
	response = client.post('/login', json={'username': username, 'password': password})
	assert response.status_code == 200
	assert 'message' in response.get_json()
