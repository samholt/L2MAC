import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user')
	assert response.status_code == 201
	assert 'user_id' in response.get_json()


def test_create_url(client):
	user_response = client.post('/create_user')
	user_id = user_response.get_json()['user_id']
	response = client.post('/create_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	user_response = client.post('/create_user')
	user_id = user_response.get_json()['user_id']
	url_response = client.post('/create_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	short_url = url_response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	user_response = client.post('/create_user')
	user_id = user_response.get_json()['user_id']
	url_response = client.post('/create_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	short_url = url_response.get_json()['short_url']
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()
	assert 'click_data' in response.get_json()
