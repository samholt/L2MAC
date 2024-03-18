import pytest
from app import app, users_db

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_set_profile_picture(client):
	response = client.post('/signup', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	response = client.post('/user/test@example.com/profile_picture', json={'profile_picture': 'picture.jpg'})
	assert response.status_code == 200
	assert users_db['test@example.com']['profile_picture'] == 'picture.jpg'


def test_set_status_message(client):
	response = client.post('/signup', json={'email': 'test2@example.com', 'password': 'password'})
	assert response.status_code == 201
	response = client.post('/user/test2@example.com/status_message', json={'status_message': 'Hello, world!'})
	assert response.status_code == 200
	assert users_db['test2@example.com']['status_message'] == 'Hello, world!'


def test_update_privacy_settings(client):
	response = client.post('/signup', json={'email': 'test3@example.com', 'password': 'password'})
	assert response.status_code == 201
	response = client.post('/user/test3@example.com/privacy_settings', json={'privacy_settings': {'details_visible': False, 'last_seen_visible': False}})
	assert response.status_code == 200
	assert users_db['test3@example.com']['privacy_settings'] == {'details_visible': False, 'last_seen_visible': False}
