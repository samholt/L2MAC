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
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'user_id': 'user1'})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()

@pytest.mark.usefixtures('reset_db')
def test_redirect_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'user_id': 'user1'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

@pytest.mark.usefixtures('reset_db')
def test_get_analytics(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'user_id': 'user1'})
	response = client.get('/analytics', json={'user_id': 'user1'})
	assert response.status_code == 200
	assert len(response.get_json()) == 1
	assert response.get_json()[0]['clicks'] == 0
	assert response.get_json()[0]['original_url'] == 'https://www.google.com'
