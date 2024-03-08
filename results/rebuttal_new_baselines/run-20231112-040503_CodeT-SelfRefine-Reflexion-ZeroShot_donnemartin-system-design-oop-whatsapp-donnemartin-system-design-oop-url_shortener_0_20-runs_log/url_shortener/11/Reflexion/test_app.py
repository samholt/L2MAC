import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def init_db():
	app.urls = {}
	app.users = {}

@pytest.mark.usefixtures('init_db')
def test_shorten_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

@pytest.mark.usefixtures('init_db')
def test_redirect_to_url(client):
	short_url = 'ABCDE'
	app.urls[short_url] = app.URL('https://www.google.com', short_url, datetime.datetime.now() + datetime.timedelta(days=30), 0)
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

@pytest.mark.usefixtures('init_db')
def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'message' in response.get_json()

@pytest.mark.usefixtures('init_db')
def test_login(client):
	app.users['test'] = app.User('test', 'test', {})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'message' in response.get_json()
