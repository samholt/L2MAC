import pytest
from views import app, url_db
from models import User, URL

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_set_expiration(client):
	response = client.post('/register', json={'username': 'test1', 'password': 'test1', 'is_admin': False})
	assert response.status_code == 200
	response = client.post('/login', json={'username': 'test1', 'password': 'test1'})
	assert response.status_code == 200
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	response = client.post(f'/set_expiration/{short_url}', json={'expiration_date': '2022-12-31T23:59:59'})
	assert response.status_code == 200
	assert url_db[short_url].expiration_date == '2022-12-31T23:59:59'


def test_redirect_to_expired_url(client):
	response = client.post('/register', json={'username': 'test2', 'password': 'test2', 'is_admin': False})
	assert response.status_code == 200
	response = client.post('/login', json={'username': 'test2', 'password': 'test2'})
	assert response.status_code == 200
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	response = client.post(f'/set_expiration/{short_url}', json={'expiration_date': '2000-01-01T00:00:00'})
	assert response.status_code == 200
	response = client.get(f'/{short_url}')
	assert response.status_code == 410
