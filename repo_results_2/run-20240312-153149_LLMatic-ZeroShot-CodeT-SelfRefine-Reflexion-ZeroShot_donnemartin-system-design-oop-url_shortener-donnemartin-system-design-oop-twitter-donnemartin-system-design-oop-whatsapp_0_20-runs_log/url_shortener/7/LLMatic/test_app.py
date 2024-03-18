import pytest
from flask import Flask, json
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in json.loads(response.data)


def test_redirect_to_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200


def test_create_account(client):
	response = client.post('/create_account', json={'username': 'test_user'})
	assert response.status_code == 200


def test_admin_dashboard_route(client):
	response = client.get('/admin/dashboard')
	assert response.status_code == 200
