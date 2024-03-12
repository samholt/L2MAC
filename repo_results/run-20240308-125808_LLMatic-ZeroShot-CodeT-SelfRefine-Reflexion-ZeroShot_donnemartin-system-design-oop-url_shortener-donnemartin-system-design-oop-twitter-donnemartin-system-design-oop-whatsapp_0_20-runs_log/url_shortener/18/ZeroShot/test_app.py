import pytest
import app
from flask import Flask
from datetime import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def init_db():
	app.DB = {}

@pytest.mark.parametrize('url, shortened, expiration', [
	('https://www.google.com', 'ggl', datetime.now()),
	('https://www.facebook.com', 'fb', datetime.now()),
])
def test_shorten_url(client, init_db, url, shortened, expiration):
	response = client.post('/shorten', json={'url': url, 'shortened': shortened, 'expiration': expiration})
	assert response.status_code == 200
	assert app.DB[shortened].original == url

@pytest.mark.parametrize('shortened', ['ggl', 'fb'])
def test_redirect_url(client, init_db, shortened):
	app.DB[shortened] = app.URL('https://www.google.com', shortened, 0, [], datetime.now())
	response = client.get(f'/{shortened}')
	assert response.status_code == 302
	assert app.DB[shortened].clicks == 1
