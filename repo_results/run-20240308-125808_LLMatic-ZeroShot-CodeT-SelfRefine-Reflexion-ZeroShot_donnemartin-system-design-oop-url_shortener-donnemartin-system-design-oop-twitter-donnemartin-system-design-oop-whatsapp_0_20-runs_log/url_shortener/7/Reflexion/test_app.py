import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('original_url', [
	'http://example.com',
	'https://google.com',
	'http://test.com'
])
def test_shorten_url(client, original_url):
	response = client.post('/shorten_url', json={'original_url': original_url})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

@pytest.mark.parametrize('short_url', [
	'ABCDE',
	'12345',
	'XYZ12'
])
def test_redirect_to_url(client, short_url):
	app.urls[short_url] = app.URL('http://example.com', short_url, datetime.datetime.now() + datetime.timedelta(days=30), 0)
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

@pytest.mark.parametrize('username, password', [
	('user1', 'pass1'),
	('user2', 'pass2'),
	('user3', 'pass3')
])
def test_register(client, username, password):
	response = client.post('/register', json={'username': username, 'password': password})
	assert response.status_code == 200
	assert 'message' in response.get_json()

@pytest.mark.parametrize('username, password', [
	('user1', 'pass1'),
	('user2', 'pass2'),
	('user3', 'pass3')
])
def test_login(client, username, password):
	app.users[username] = app.User(username, password, {})
	response = client.post('/login', json={'username': username, 'password': password})
	assert response.status_code == 200
	assert 'message' in response.get_json()
