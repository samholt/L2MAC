import pytest
import app
from user import User
from chat import Chat

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 201
	assert 'id' in response.get_json()
	assert response.get_json()['email'] == 'test@test.com'


def test_login(client):
	client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 200
	assert 'id' in response.get_json()
	assert response.get_json()['email'] == 'test@test.com'


def test_create_chat(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	user_id = response.get_json()['id']
	response = client.post(f'/users/{user_id}/chats', json={'name': 'Test Chat'})
	assert response.status_code == 201
	assert 'id' in response.get_json()
	assert response.get_json()['name'] == 'Test Chat'
	assert len(response.get_json()['users']) == 1
