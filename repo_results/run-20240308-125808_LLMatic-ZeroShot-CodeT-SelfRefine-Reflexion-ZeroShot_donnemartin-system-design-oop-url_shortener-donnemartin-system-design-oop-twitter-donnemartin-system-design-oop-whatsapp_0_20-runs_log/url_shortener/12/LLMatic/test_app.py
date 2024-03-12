import pytest
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com', 'username': 'test_user'})
	assert response.status_code == 200


def test_redirect_to_original_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com', 'username': 'test_user'})
	short_url = response.get_data(as_text=True)
	response = client.get('/' + short_url)
	assert response.status_code == 302


def test_analytics(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com', 'username': 'test_user'})
	short_url = response.get_data(as_text=True)
	response = client.get('/analytics/' + short_url)
	assert response.status_code == 200


def test_admin_dashboard(client):
	response = client.get('/admin/dashboard')
	assert response.status_code == 200


def test_delete_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com', 'username': 'test_user'})
	short_url = response.get_data(as_text=True)
	response = client.post('/admin/delete_url', json={'username': 'test_user', 'url': short_url})
	assert response.status_code == 200


def test_delete_user(client):
	response = client.post('/admin/delete_user', json={'username': 'test_user'})
	assert response.status_code == 200
