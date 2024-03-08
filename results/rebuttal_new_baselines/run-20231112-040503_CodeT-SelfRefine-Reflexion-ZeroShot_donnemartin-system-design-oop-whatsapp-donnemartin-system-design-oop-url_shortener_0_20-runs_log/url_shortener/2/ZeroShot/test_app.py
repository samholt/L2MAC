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

@pytest.mark.parametrize('url, shortened, expiration', [
	('https://www.google.com', 'goog', (datetime.now() + timedelta(days=1)).isoformat()),
	('https://www.example.com', 'exmpl', (datetime.now() + timedelta(days=1)).isoformat())
])
def test_shorten_url(client, reset_db, url, shortened, expiration):
	response = client.post('/shorten', data=json.dumps({'url': url, 'shortened': shortened, 'expiration': expiration}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['data']['original'] == url
	assert response.get_json()['data']['shortened'] == shortened

@pytest.mark.parametrize('shortened', ['goog', 'exmpl'])
def test_redirect_url(client, reset_db, shortened):
	app.DB[shortened] = app.URL(original='https://www.google.com', shortened=shortened, clicks=0, click_data=[], expiration=datetime.now() + timedelta(days=1))
	response = client.get(f'/{shortened}')
	assert response.status_code == 302
	assert app.DB[shortened].clicks == 1
