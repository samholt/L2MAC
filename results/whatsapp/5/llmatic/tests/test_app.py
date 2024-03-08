import pytest
from views.app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register')
	assert response.status_code == 200


def test_login(client):
	response = client.post('/login')
	assert response.status_code == 200


def test_profile(client):
	response = client.get('/profile')
	assert response.status_code == 200


def test_contacts(client):
	response = client.get('/contacts')
	assert response.status_code == 200


def test_messages(client):
	response = client.get('/messages')
	assert response.status_code == 200


def test_groups(client):
	response = client.get('/groups')
	assert response.status_code == 200


def test_statuses(client):
	response = client.get('/statuses')
	assert response.status_code == 200
