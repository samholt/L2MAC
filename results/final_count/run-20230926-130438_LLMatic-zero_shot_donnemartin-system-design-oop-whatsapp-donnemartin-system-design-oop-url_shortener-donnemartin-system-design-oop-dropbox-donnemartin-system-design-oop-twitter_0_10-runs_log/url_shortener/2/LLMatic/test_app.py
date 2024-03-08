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
	assert response.data == b'Hello, World!'


def test_redirect_to_original_url(client):
	response = client.get('/abc123')
	assert response.status_code == 404


def test_shorten_url(client):
	response = client.post('/shorten', data={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_view_analytics(client):
	response = client.get('/analytics/abc123')
	assert response.status_code == 200
	assert 'analytics' in response.get_json()


def test_manage_account(client):
	response = client.post('/account', data={'action': 'create', 'username': 'testuser', 'password': 'testpass'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Account created successfully.'

	response = client.post('/account', data={'action': 'view_urls', 'username': 'testuser'})
	assert response.status_code == 200
	assert 'urls' in response.get_json()

	response = client.post('/account', data={'action': 'delete', 'username': 'testuser'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Account deleted successfully.'


def test_admin_dashboard(client):
	response = client.get('/admin')
	assert response.status_code == 200
	assert 'urls' in response.get_json()
	assert 'users' in response.get_json()
	assert 'performance' in response.get_json()


def test_delete_url(client):
	client.post('/admin', data={'action': 'delete_url', 'short_url': 'abc123'})
	response = client.get('/abc123')
	assert response.status_code == 404


def test_delete_user(client):
	client.post('/admin', data={'action': 'delete_user', 'username': 'testuser'})
	response = client.get('/admin')
	assert 'testuser' not in response.get_json()['users']

