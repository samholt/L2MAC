import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'short_url': 'ggl', 'user': 'test', 'expiration': '2022-12-31T23:59:59'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'URL shortened successfully', 'short_url': 'ggl'}


def test_redirect_url(client):
	response = client.get('/ggl')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.get('/analytics?user=test')
	assert response.status_code == 200
	data = json.loads(response.data)
	assert len(data) == 1
	assert data[0]['original'] == 'https://www.google.com'
	assert data[0]['shortened'] == 'ggl'
