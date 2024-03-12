import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return app.User('test', 'password', [])

@pytest.fixture
def url(user):
	return app.URL('https://www.google.com', '12345', user.username, 0, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=1))

def test_shorten_url(client, user):
	app.users[user.username] = user
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': user.username, 'expires_at': (datetime.datetime.now() + datetime.timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

def test_redirect_url(client, url):
	app.urls[url.short] = url
	response = client.get('/' + url.short)
	assert response.status_code == 302
	assert url.clicks == 1

def test_create_user(client):
	response = client.post('/user', json={'username': 'test', 'password': 'password'})
	assert response.status_code == 201
	assert 'message' in response.get_json()

def test_get_user(client, user):
	app.users[user.username] = user
	response = client.get('/user/' + user.username)
	assert response.status_code == 200
	assert 'username' in response.get_json()
	assert 'urls' in response.get_json()
