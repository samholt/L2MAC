import pytest
import url_shortener
import datetime

@pytest.fixture
def client():
	url_shortener.app.config['TESTING'] = True
	with url_shortener.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	url_shortener.urls_db = {}
	url_shortener.users_db = {}

@pytest.mark.usefixtures('reset_db')
def test_shorten_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

@pytest.mark.usefixtures('reset_db')
def test_redirect_to_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

@pytest.mark.usefixtures('reset_db')
def test_expired_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'expiration_date': (datetime.datetime.now() - datetime.timedelta(days=1)).isoformat()})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
