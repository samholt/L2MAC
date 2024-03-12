import pytest
import app
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_database():
	app.DATABASE.clear()
	app.USER_DATABASE.clear()
	app.ADMIN_DATABASE.clear()
	app.ANALYTICS_DATABASE.clear()

@pytest.mark.usefixtures('reset_database')
def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()

@pytest.mark.usefixtures('reset_database')
def test_redirect_url(client):
	client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = list(app.DATABASE.keys())[0]
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

@pytest.mark.usefixtures('reset_database')
def test_get_analytics(client):
	client.post('/users', json={'username': 'test', 'password': 'test'})
	client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test'})
	response = client.get('/analytics', json={'user': 'test'})
	assert response.status_code == 200

@pytest.mark.usefixtures('reset_database')
def test_create_user(client):
	response = client.post('/users', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201

@pytest.mark.usefixtures('reset_database')
def test_create_admin(client):
	response = client.post('/admin', json={'username': 'admin', 'password': 'admin'})
	assert response.status_code == 201

@pytest.mark.usefixtures('reset_database')
def test_admin_dashboard(client):
	client.post('/admin', json={'username': 'admin', 'password': 'admin'})
	client.post('/shorten', json={'url': 'https://www.google.com'})
	response = client.get('/admin/dashboard', json={'admin': 'admin'})
	assert response.status_code == 200

