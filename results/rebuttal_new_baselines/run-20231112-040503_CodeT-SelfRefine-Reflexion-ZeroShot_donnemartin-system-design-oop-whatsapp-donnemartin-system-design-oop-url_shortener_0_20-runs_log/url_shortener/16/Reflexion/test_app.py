import pytest
import app
from flask import json
from datetime import datetime, timedelta
import pytz

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_url():
	return {
		'original_url': 'https://www.google.com',
		'short_url': 'goog123',
		'user_id': 'user1',
		'clicks': 0,
		'expires_at': (datetime.now(pytz.UTC) + timedelta(days=1)).isoformat()
	}


def test_shorten_url(client, sample_url):
	response = client.post('/shorten_url', data=json.dumps(sample_url), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == sample_url


def test_redirect_url(client, sample_url):
	client.post('/shorten_url', data=json.dumps(sample_url), content_type='application/json')
	response = client.get('/' + sample_url['short_url'])
	assert response.status_code == 302
	assert response.location == sample_url['original_url']


def test_get_analytics(client, sample_url):
	client.post('/shorten_url', data=json.dumps(sample_url), content_type='application/json')
	response = client.get('/analytics/' + sample_url['short_url'])
	assert response.status_code == 200
	assert response.get_json() == sample_url


def test_url_not_found(client):
	response = client.get('/nonexistent')
	assert response.status_code == 404


def test_url_expired(client, sample_url):
	expired_url = sample_url.copy()
	expired_url['expires_at'] = (datetime.now(pytz.UTC) - timedelta(days=1)).isoformat()
	client.post('/shorten_url', data=json.dumps(expired_url), content_type='application/json')
	response = client.get('/' + expired_url['short_url'])
	assert response.status_code == 410
