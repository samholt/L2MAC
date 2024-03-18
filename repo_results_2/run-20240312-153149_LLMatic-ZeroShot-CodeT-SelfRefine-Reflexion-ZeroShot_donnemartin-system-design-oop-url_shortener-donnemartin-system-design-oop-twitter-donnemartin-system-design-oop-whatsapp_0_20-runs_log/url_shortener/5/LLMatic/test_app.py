import pytest
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_page_not_found(client):
	response = client.get('/nonexistentpage')
	assert response.status_code == 404
	assert response.data == b'Page not found'

def test_internal_server_error(client):
	response = client.get('/nonexistentpage')
	assert response.status_code == 404
	assert response.data == b'Page not found'
