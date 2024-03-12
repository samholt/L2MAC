import pytest
import app
from url_shortener import url_db
from user import User

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200


def test_redirect_to_original(client):
	url_db['test'] = {'url': 'http://example.com', 'expiration': None}
	response = client.get('/test')
	assert response.status_code == 302


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'http://example.com'})
	assert response.status_code == 200


def test_manage_user(client):
	response = client.post('/user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	response = client.put('/user', json={'username': 'test', 'password': 'test2'})
	assert response.status_code == 200
	response = client.delete('/user', json={'username': 'test'})
	assert response.status_code == 200


def test_admin_dashboard(client):
	response = client.get('/admin')
	assert response.status_code == 200


def test_admin_url_stats(client):
	url_db['test'] = {'url': 'http://example.com', 'expiration': None}
	response = client.get('/admin/test')
	assert response.status_code == 200
