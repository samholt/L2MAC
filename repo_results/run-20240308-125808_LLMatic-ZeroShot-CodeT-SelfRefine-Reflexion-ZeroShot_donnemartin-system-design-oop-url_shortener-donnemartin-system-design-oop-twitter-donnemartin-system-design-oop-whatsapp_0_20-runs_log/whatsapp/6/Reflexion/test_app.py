import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': '1', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}


def test_get_user(client):
	response = client.get('/user/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'email': 'test@test.com', 'password': 'test', 'profile_picture': None, 'status_message': None, 'privacy_settings': None, 'contacts': None}


def test_create_chat(client):
	response = client.post('/chat', json={'id': '1', 'name': 'Test Chat'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}


def test_get_chat(client):
	response = client.get('/chat/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'name': 'Test Chat', 'members': None, 'messages': None}
