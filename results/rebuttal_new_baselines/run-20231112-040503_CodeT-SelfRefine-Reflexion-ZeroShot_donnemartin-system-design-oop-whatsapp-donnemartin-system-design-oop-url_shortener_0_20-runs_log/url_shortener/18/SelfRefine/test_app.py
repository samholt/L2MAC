import pytest
import app
from flask import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {}

@pytest.mark.parametrize('url, shortened', [
	('https://www.google.com', 'goog'),
	('https://www.facebook.com', 'fb'),
	('https://www.twitter.com', 'tw')
])
def test_shorten_url(client, reset_db, url, shortened):
	expiration = (datetime.now() + timedelta(days=1)).isoformat()
	response = client.post('/shorten', data=json.dumps({'url': url, 'shortened': shortened, 'expiration': expiration}), content_type='application/json')
	assert response.status_code == 200
	assert app.DB[shortened].original == url

	# Test redirect and analytics after shortening URL
	response = client.get(f'/{shortened}')
	assert response.status_code == 302
	assert app.DB[shortened].clicks == 1

	response = client.get(f'/analytics/{shortened}')
	assert response.status_code == 200
	assert app.DB[shortened].clicks == response.get_json()['data']['clicks']
