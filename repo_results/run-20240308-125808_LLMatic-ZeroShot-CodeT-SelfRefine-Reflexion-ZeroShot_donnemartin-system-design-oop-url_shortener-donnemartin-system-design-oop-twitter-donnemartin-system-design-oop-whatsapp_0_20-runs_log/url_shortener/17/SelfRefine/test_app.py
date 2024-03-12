import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 201
	data = json.loads(response.data)
	assert 'shortened_url' in data

	response = client.get('/' + data['shortened_url'])
	assert response.status_code == 302

	response = client.get('/analytics/' + data['shortened_url'])
	assert response.status_code == 200
	data = json.loads(response.data)
	assert data['clicks'] == 1

	response = client.get('/' + data['shortened_url'])
	assert response.status_code == 302

	response = client.get('/analytics/' + data['shortened_url'])
	assert response.status_code == 200
	data = json.loads(response.data)
	assert data['clicks'] == 2

	response = client.post('/shorten', json={'url': 'https://www.google.com', 'expiration': '2020-01-01 00:00:00'})
	assert response.status_code == 201
	data = json.loads(response.data)
	assert 'shortened_url' in data

	response = client.get('/' + data['shortened_url'])
	assert response.status_code == 404

	response = client.post('/shorten', json={'url': 'https://www.google.com', 'custom': data['shortened_url']})
	assert response.status_code == 400

	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'shortened_url' in data
