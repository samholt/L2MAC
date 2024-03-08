import pytest
import app
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_url():
	return {
		'original': 'https://www.google.com',
		'shortened': 'goog',
		'expiration': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
	}

def test_shorten_url(client, sample_url):
	response = client.post('/shorten', json=sample_url)
	assert response.status_code == 200
	assert response.get_json() == {'shortened_url': 'goog'}

def test_redirect_to_original(client, sample_url):
	client.post('/shorten', json=sample_url)
	response = client.get('/goog')
	assert response.status_code == 302

def test_get_analytics(client, sample_url):
	client.post('/shorten', json=sample_url)
	client.get('/goog')
	response = client.get('/analytics/goog')
	assert response.status_code == 200
	assert len(response.get_json()['click_data']) == 1
