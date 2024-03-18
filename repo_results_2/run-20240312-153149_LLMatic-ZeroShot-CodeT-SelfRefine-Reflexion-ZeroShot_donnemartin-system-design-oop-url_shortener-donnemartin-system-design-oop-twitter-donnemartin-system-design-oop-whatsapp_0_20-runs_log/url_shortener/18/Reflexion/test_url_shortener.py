import pytest
import url_shortener

@pytest.fixture
def client():
	url_shortener.app.config['TESTING'] = True
	with url_shortener.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'


def test_redirect_url_not_found(client):
	response = client.get('/nonexistent')
	assert response.status_code == 404
