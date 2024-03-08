import pytest
import app
from flask import Flask
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def url():
	return app.URL(
		original='https://www.google.com',
		shortened='12345678',
		user='test',
		clicks=0,
		created_at=datetime.now(),
		expires_at=datetime.now() + timedelta(days=1)
	)

def test_shorten_url(client, url):
	response = client.post('/shorten', json=url.__dict__)
	assert response.status_code == 201
	assert 'shortened' in response.get_json()


def test_redirect_url(client, url):
	app.DB[url.shortened] = url
	response = client.get(f'/{url.shortened}')
	assert response.status_code == 302
	assert app.DB[url.shortened].clicks == 1


def test_redirect_url_not_found_or_expired(client):
	response = client.get('/nonexistent')
	assert response.status_code == 404
	assert 'error' in response.get_json()


def test_url_details(client, url):
	app.DB[url.shortened] = url
	response = client.get(f'/details/{url.shortened}')
	assert response.status_code == 200
	assert response.get_json() == url.__dict__
