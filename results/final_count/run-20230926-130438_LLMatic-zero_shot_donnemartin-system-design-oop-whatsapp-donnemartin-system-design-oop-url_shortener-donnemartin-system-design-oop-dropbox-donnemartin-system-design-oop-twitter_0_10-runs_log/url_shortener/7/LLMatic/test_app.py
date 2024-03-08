import pytest
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.data == b'Hello, World!'


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'url': 'http://example.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_to_url(client):
	response = client.post('/shorten_url', json={'url': 'http://example.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_analytics(client):
	response = client.post('/shorten_url', json={'url': 'http://example.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()
	assert 'details' in response.get_json()


def test_create_account(client):
	response = client.post('/create_account', json={'username': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Account created successfully.'


def test_view_all_urls(client):
	response = client.get('/admin/view_all_urls')
	assert response.status_code == 200
