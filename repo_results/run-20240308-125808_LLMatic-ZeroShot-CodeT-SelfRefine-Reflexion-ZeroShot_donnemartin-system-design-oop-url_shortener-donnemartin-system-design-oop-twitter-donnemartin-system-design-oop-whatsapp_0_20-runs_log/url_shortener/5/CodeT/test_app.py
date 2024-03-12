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
	('https://www.facebook.com', 'fb', (datetime.now() + timedelta(days=1)).isoformat()),
])
def test_shorten_url(client, reset_db, url, shortened, expiration):
	response = client.post('/shorten', data=json.dumps({'url': url, 'shortened': shortened, 'expiration': expiration}), content_type='application/json')
	assert response.status_code == 200
	assert app.DB[shortened].original == url
	assert app.DB[shortened].shortened == shortened
	assert app.DB[shortened].clicks == 0
	assert app.DB[shortened].click_data == []
	assert app.DB[shortened].expiration == datetime.fromisoformat(expiration)

@pytest.mark.parametrize('shortened', [
	('goog'),
	('fb'),
])
def test_redirect_url(client, reset_db, shortened):
	app.DB[shortened] = app.URL('https://www.google.com', shortened, 0, [], datetime.now() + timedelta(days=1))
	response = client.get(f'/{shortened}')
	assert response.status_code == 302
	assert app.DB[shortened].clicks == 1
	assert len(app.DB[shortened].click_data) == 1
