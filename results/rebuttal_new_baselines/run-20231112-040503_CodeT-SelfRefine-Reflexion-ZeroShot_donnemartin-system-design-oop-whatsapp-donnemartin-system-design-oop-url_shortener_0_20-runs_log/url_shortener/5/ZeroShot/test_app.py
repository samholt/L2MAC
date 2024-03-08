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
	app.users = {}
	app.urls = {}

@pytest.mark.usefixtures('setup')
def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'test' in app.users

@pytest.mark.usefixtures('setup')
def test_login(client):
	app.users['test'] = app.User('test', 'test', {})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200

@pytest.mark.usefixtures('setup')
def test_shorten(client):
	response = client.post('/shorten', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert len(app.urls) == 1

@pytest.mark.usefixtures('setup')
def test_redirect(client):
	app.urls['test'] = app.URL('https://www.google.com', 'test', None, 0, [], None)
	response = client.get('/test')
	assert response.status_code == 302

@pytest.mark.usefixtures('setup')
def test_analytics(client):
	app.users['test'] = app.User('test', 'test', {})
	app.urls['test'] = app.URL('https://www.google.com', 'test', 'test', 0, [], None)
	app.users['test'].urls['test'] = app.urls['test']
	response = client.get('/analytics', json={'user': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'test': {'clicks': 0, 'click_data': []}}
