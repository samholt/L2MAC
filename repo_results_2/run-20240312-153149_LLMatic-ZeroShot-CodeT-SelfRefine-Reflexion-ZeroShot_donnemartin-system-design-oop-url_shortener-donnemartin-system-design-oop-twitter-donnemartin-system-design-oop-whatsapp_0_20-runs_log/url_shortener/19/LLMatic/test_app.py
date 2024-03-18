import pytest
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200


def test_short_url_redirect(client):
	response = client.get('/nonexistent')
	assert response.status_code == 404


def test_admin_dashboard(client):
	response = client.get('/admin')
	assert response.status_code == 200


def test_register(client):
	response = client.post('/register', data={'username': 'test', 'password': 'test'})
	assert response.status_code == 200


def test_login(client):
	response = client.post('/login', data={'username': 'test', 'password': 'test'})
	assert response.status_code == 200


def test_add_url(client):
	response = client.post('/add_url', data={'username': 'test', 'url': 'https://www.google.com'})
	assert response.status_code == 200
