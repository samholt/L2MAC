import pytest
from app import app, DB, URL
from datetime import datetime, timedelta
import uuid

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	DB.clear()

@pytest.fixture
def sample_url():
	shortened_url = str(uuid.uuid4())[:8]
	DB[shortened_url] = URL('http://example.com', shortened_url, 'test_user', [], datetime.now() + timedelta(days=1))
	return shortened_url

def test_shorten_url(client, reset_db):
	response = client.post('/shorten', json={'url': 'http://example.com', 'user': 'test_user', 'expiration': '2022-12-31T23:59:59'})
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()

def test_redirect_to_original(client, sample_url):
	response = client.get(f'/{sample_url}')
	assert response.status_code == 302
	assert DB[sample_url].clicks

def test_get_analytics(client, sample_url):
	response = client.get('/analytics?user=test_user')
	assert response.status_code == 200
	assert response.get_json()['urls']
