import pytest
import app
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_data():
	app.urls = {}
	app.users = {}

@pytest.mark.usefixtures('reset_data')
def test_shorten_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'user': 'test_user', 'expires_at': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_redirect_to_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'user': 'test_user', 'expires_at': (datetime.now() + timedelta(days=1)).isoformat()})
	short_url = response.get_json()['short_url']

	response = client.get(f'/{short_url}')
	assert response.status_code == 302

@pytest.mark.usefixtures('reset_data')
def test_get_analytics(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'user': 'test_user', 'expires_at': (datetime.now() + timedelta(days=1)).isoformat()})
	short_url = response.get_json()['short_url']

	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()
	assert 'location' in response.get_json()
