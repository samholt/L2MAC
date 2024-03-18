import pytest
import requests
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.mark.parametrize('url, shortened', [
	('http://example.com', 'exmpl'),
	('https://google.com', 'ggl'),
])
def test_shorten_url(client, url, shortened):
	response = client.post('/shorten', json={'url': url, 'shortened': shortened})
	assert response.status_code == 201
	assert response.get_json() == {'shortened_url': shortened}

	response = client.get(f'/{shortened}')
	assert response.status_code == 302
	assert response.headers['Location'] == url

	response = client.get(f'/analytics/{shortened}')
	assert response.status_code == 200
	assert len(response.get_json()['clicks']) == 1

	response = client.post('/shorten', json={'url': url, 'shortened': shortened})
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Shortened URL is already in use'}

	response = client.post('/shorten', json={'url': 'invalid', 'shortened': 'invalid'})
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Invalid URL'}

	response = client.get('/invalid')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'URL not found'}

	response = client.get('/analytics/invalid')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'URL not found'}
