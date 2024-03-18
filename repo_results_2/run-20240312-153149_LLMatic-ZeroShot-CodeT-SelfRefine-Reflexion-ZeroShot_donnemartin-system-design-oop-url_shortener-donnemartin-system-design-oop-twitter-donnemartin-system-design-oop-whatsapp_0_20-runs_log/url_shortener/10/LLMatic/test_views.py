import pytest
from app import app
from services import create_short_url, get_original_url

@pytest.fixture

def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200

def test_redirect(client):
	original_url = 'http://example.com'
	short_url = create_short_url('test_user', original_url)
	response = client.get('/' + short_url)
	assert response.status_code == 302
	assert response.location == original_url

def test_redirect_not_found(client):
	response = client.get('/nonexistent')
	assert response.status_code == 404
