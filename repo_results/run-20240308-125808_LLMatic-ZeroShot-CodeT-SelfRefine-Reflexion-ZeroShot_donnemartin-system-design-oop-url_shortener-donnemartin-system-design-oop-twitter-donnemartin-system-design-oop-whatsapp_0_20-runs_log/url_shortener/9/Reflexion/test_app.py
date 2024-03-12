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

	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'

	response = client.get(f'/{short_url}')
	assert response.status_code == 404

	response = client.post('/shorten', json={'url': 'https://www.example.com', 'expires_at': (datetime.datetime.now() + datetime.timedelta(minutes=1)).isoformat()})
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.example.com'
