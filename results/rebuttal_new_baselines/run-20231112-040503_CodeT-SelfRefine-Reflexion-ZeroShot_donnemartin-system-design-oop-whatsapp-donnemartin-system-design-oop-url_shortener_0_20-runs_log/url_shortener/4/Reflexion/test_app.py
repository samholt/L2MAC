import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten_url', data=json.dumps({'original_url': 'https://www.google.com'}), content_type='application/json')
	assert response.status_code == 201
	short_url = json.loads(response.data)['short_url']
	assert len(short_url) == 8


def test_redirect_url(client):
	response = client.post('/shorten_url', data=json.dumps({'original_url': 'https://www.google.com'}), content_type='application/json')
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'


def test_expired_url(client):
	response = client.post('/shorten_url', data=json.dumps({'original_url': 'https://www.google.com'}), content_type='application/json')
	short_url = json.loads(response.data)['short_url']
	app.DATABASE[short_url].expiration_time = app.datetime.now(app.pytz.utc) - app.timedelta(days=1)
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
