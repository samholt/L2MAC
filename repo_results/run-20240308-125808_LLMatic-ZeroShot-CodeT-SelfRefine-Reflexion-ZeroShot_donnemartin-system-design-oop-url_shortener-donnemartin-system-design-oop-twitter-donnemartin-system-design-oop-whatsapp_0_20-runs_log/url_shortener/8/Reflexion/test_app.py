import pytest
from app import app, DB, URL
from datetime import datetime, timedelta

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
	return URL(original='https://www.google.com', shortened='goog', clicks=0, created_at=datetime.now(), expires_at=datetime.now() + timedelta(days=1))


def test_shorten_url(client, reset_db, sample_url):
	response = client.post('/shorten', json={'url': sample_url.original, 'short': sample_url.shortened, 'expires_at': sample_url.expires_at})
	assert response.status_code == 200
	assert DB[sample_url.shortened] == sample_url


def test_redirect_url(client, reset_db, sample_url):
	DB[sample_url.shortened] = sample_url
	response = client.get(f'/{sample_url.shortened}')
	assert response.status_code == 302
	assert DB[sample_url.shortened].clicks == 1


def test_get_analytics(client, reset_db, sample_url):
	DB[sample_url.shortened] = sample_url
	response = client.get(f'/analytics/{sample_url.shortened}')
	data = response.get_json()
	assert response.status_code == 200
	assert data['original_url'] == sample_url.original
	assert data['short_url'] == sample_url.shortened
	assert data['clicks'] == sample_url.clicks
	assert data['created_at'] == sample_url.created_at
	assert data['expires_at'] == sample_url.expires_at
