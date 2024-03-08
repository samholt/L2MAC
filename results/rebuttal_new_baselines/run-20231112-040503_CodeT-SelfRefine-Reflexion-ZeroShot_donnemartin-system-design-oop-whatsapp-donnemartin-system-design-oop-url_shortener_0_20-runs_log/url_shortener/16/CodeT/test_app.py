import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert data['data']['original'] == 'https://www.google.com'
	assert data['data']['shortened'] == 'ggl'


def test_redirect_url(client):
	response = client.get('/ggl')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.get('/analytics/ggl')
	assert response.status_code == 200
	data = json.loads(response.data)
	assert data['data']['clicks'] == 1
