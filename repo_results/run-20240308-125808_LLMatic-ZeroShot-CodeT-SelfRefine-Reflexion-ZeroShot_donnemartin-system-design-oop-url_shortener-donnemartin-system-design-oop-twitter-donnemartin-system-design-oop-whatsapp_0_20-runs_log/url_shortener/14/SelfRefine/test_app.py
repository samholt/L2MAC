import pytest
import app
from flask import json
from datetime import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.yahoo.com', 'shortened': 'yh', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'URL shortened successfully'


def test_redirect_url(client):
	response = client.get('/ggl')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.get('/analytics/ggl')
	assert response.status_code == 200
	assert json.loads(response.data)['data']['clicks'] == 1
	assert datetime.fromisoformat(json.loads(response.data)['data']['expiration']) > datetime.now()
