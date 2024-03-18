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
	app.urls_db = {}
	app.users_db = {}

@pytest.mark.usefixtures('init_db')
def test_shorten_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

@pytest.mark.usefixtures('init_db')
def test_redirect_to_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

@pytest.mark.usefixtures('init_db')
def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'message' in response.get_json()

@pytest.mark.usefixtures('init_db')
def test_get_user_urls(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.get('/user/test/urls')
	assert response.status_code == 200
	assert 'urls' in response.get_json()

@pytest.mark.usefixtures('init_db')
def test_delete_user_url(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	app.users_db['test'].urls[short_url] = app.urls_db[short_url]
	response = client.delete('/user/test/url/' + short_url)
	assert response.status_code == 200
	assert 'message' in response.get_json()
