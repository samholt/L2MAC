import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'shortened': 'goog', 'user': 'test', 'expiration': '2022-12-31 23:59:59'}), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'URL shortened successfully'


def test_redirect_url(client):
	response = client.get('/goog')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.get('/analytics', data=json.dumps({'user': 'test'}), content_type='application/json')
	assert response.status_code == 200


def test_get_admin(client):
	response = client.get('/admin')
	assert response.status_code == 200
