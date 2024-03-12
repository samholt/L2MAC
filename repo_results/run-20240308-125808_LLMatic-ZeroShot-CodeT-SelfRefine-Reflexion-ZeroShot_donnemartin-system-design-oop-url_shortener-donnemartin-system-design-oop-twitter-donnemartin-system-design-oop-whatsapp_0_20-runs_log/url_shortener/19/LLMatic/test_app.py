import pytest
from app import app
from database import Database

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture(autouse=True)
def setup_db():
	# Setup
	db = Database()
	db.insert('users', 'testuser', {'password': 'password', 'urls': ['testurl']})
	db.insert('urls', 'testurl', {'url': 'http://example.com', 'expiration_date': None})
	db.insert('analytics', 'testurl', {'clicks': 0, 'details': []})
	# Teardown
	yield
	db.delete('users', 'testuser')
	db.delete('urls', 'testurl')
	db.delete('analytics', 'testurl')


def test_shorten_url(client):
	response = client.post('/shorten', json={'original_url': 'http://example.com'})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_redirect_to_url(client):
	response = client.get('/testurl')
	assert response.status_code == 302
	assert response.headers['Location'] == 'http://example.com'


def test_get_user_urls(client):
	response = client.get('/user/testuser/urls')
	assert response.status_code == 200
	assert response.get_json() == ['testurl']


def test_get_user_analytics(client):
	response = client.get('/user/testuser/analytics')
	assert response.status_code == 200
	assert response.get_json() == {'testurl': 0}


def test_admin_dashboard(client):
	response = client.get('/admin/dashboard')
	assert response.status_code == 200
	assert 'users' in response.get_json()
	assert 'urls' in response.get_json()
