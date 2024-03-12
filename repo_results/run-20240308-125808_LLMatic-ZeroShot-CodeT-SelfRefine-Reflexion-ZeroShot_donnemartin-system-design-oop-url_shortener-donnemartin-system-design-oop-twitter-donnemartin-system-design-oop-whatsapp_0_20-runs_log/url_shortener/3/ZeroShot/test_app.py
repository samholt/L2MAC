import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'URL shortened successfully'}

	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Shortened URL already in use'}

	response = client.post('/shorten', json={'url': 'invalid_url', 'shortened': 'invalid'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Invalid URL'}


def test_redirect_url(client):
	client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog'})
	response = client.get('/goog')
	assert response.status_code == 302

	response = client.get('/invalid')
	assert response.status_code == 404
	assert json.loads(response.data) == {'error': 'URL not found'}


def test_get_analytics(client):
	client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog'})
	client.get('/goog')
	response = client.get('/analytics/goog')
	data = json.loads(response.data)
	assert response.status_code == 200
	assert data['clicks'] == 1
	assert len(data['click_data']) == 1

	response = client.get('/analytics/invalid')
	assert response.status_code == 404
	assert json.loads(response.data) == {'error': 'URL not found'}
