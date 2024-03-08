import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def setup_data():
	app.users = {}
	app.urls = {}
	user = app.User(username='test', password='test', urls=[])
	app.users['test'] = user
	url = app.URL(original='https://www.google.com', short='abcde', user='test', clicks=0, created_at=datetime.datetime.now())
	app.urls['abcde'] = url

@pytest.mark.parametrize('short_url, expected_status', [('abcde', 302), ('invalid', 404)])
def test_redirect_url(client, setup_data, short_url, expected_status):
	response = client.get(f'/{short_url}')
	assert response.status_code == expected_status

@pytest.mark.parametrize('username, password, expected_status', [('test', 'test', 201), ('test', 'test', 400)])
def test_create_user(client, setup_data, username, password, expected_status):
	response = client.post('/user', json={'username': username, 'password': password})
	assert response.status_code == expected_status

@pytest.mark.parametrize('url, username, expected_status', [('https://www.google.com', 'test', 200), ('https://www.google.com', 'invalid', 200)])
def test_shorten_url(client, setup_data, url, username, expected_status):
	response = client.post('/shorten', json={'url': url, 'username': username})
	assert response.status_code == expected_status
