import pytest
import app
import datetime
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {}

@pytest.mark.parametrize('url, custom, expiration, status', [
	('https://www.google.com', None, None, 200),
	('https://www.google.com', 'custom', None, 200),
	('https://www.google.com', 'custom', '2022-12-31T23:59:59', 200),
	('invalid', None, None, 400),
	('https://www.google.com', 'custom', None, 200),
	('https://www.google.com', None, 'invalid', 400),
])
def test_shorten_url(client, reset_db, url, custom, expiration, status):
	response = client.post('/shorten', data=json.dumps({'url': url, 'custom': custom, 'expiration': expiration}), content_type='application/json')
	assert response.status_code == status

	# Test creating a URL with an already existing custom URL
	if custom == 'custom':
		response = client.post('/shorten', data=json.dumps({'url': url, 'custom': custom, 'expiration': expiration}), content_type='application/json')
		assert response.status_code == 400

@pytest.mark.parametrize('shortened_url, status', [
	('custom', 302),
	('invalid', 404),
	('expired', 400),
])
def test_redirect_url(client, reset_db, shortened_url, status):
	app.DB['custom'] = app.URL(original='https://www.google.com', shortened='custom', clicks=0, click_data=[], expiration=None)
	app.DB['expired'] = app.URL(original='https://www.google.com', shortened='expired', clicks=0, click_data=[], expiration=datetime.datetime.now() - datetime.timedelta(days=1))
	response = client.get(f'/{shortened_url}')
	assert response.status_code == status
