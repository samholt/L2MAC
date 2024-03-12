import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': '2022-12-31T23:59:59'}), content_type='application/json')
	assert response.status_code == 200
	assert 'URL shortened successfully' in response.get_data(as_text=True)


def test_redirect_url(client):
	response = client.get('/ggl')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'
