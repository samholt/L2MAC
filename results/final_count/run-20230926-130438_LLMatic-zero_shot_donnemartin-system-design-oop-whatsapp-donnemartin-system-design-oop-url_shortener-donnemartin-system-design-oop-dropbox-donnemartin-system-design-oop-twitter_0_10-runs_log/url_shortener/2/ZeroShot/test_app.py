import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_redirect_to_url(client):
	response = client.post('/shorten', json={'original_url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	user_id = client.post('/users').get_json()['user_id']
	client.post('/shorten', json={'original_url': 'https://www.google.com', 'user_id': user_id})
	response = client.get('/analytics', json={'user_id': user_id})
	assert response.status_code == 200
	assert len(response.get_json()) == 1


def test_create_user(client):
	response = client.post('/users')
	assert response.status_code == 201
	assert 'user_id' in response.get_json()
