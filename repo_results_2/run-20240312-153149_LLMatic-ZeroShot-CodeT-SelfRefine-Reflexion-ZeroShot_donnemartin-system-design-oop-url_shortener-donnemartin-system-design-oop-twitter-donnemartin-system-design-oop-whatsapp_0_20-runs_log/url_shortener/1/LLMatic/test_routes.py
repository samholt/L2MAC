import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

def test_redirect_to_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

def test_view_analytics(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()

def test_create_user(client):
	response = client.post('/user/create', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Account created successfully'

def test_create_admin(client):
	response = client.post('/admin/create', json={'username': 'admin', 'password': 'admin'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Account created successfully'

def test_invalid_shorten_url(client):
	response = client.post('/shorten', json={'url': 'invalid_url'})
	assert response.status_code == 400
	assert response.get_json()['error'] == 'Invalid URL or alias already in use'

def test_invalid_user_create(client):
	response = client.post('/user/create', json={'username': '', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json()['error'] == 'Invalid username or password'

def test_invalid_admin_create(client):
	response = client.post('/admin/create', json={'username': '', 'password': 'admin'})
	assert response.status_code == 400
	assert response.get_json()['error'] == 'Invalid username or password'

