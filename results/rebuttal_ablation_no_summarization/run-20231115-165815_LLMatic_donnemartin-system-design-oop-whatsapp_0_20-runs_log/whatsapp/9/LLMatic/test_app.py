import pytest
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200
	assert b'Chat Application' in response.data


def test_update_status(client):
	response = client.post('/users/test@example.com/status', json={'status': 'online'})
	assert response.status_code == 200
	assert b'Status updated' in response.data
