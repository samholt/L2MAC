import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

# Test URL shortening

def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'shortened_url' in response.get_json()

# Test URL redirection

def test_redirect_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['shortened_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'

# Test URL expiration

def test_url_expiration(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'expiration': datetime.datetime.now().isoformat()})
	short_url = response.get_json()['shortened_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
