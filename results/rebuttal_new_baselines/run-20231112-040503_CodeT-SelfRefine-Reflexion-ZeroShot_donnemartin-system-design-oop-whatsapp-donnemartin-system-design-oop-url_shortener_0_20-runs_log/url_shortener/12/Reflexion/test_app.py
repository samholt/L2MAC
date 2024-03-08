import pytest
import app
import datetime

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


def test_get_analytics(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	response = client.get('/analytics?user=test_user')
	assert response.status_code == 200
	assert len(response.get_json()['urls']) == 1


def test_url_expiration(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'expires_at': (datetime.datetime.now() - datetime.timedelta(minutes=1)).isoformat()})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
