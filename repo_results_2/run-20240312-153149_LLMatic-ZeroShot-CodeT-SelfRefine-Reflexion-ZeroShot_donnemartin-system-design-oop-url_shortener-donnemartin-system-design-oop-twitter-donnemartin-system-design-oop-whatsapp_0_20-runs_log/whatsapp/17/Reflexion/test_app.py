import pytest
import app
from app import User, Message

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert app.users['test@test.com'].name == 'Test'

def test_login(client):
	client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200

def test_update_profile(client):
	client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	response = client.put('/update_profile', json={'email': 'test@test.com', 'password': 'test', 'profile_picture': 'test.jpg', 'status_message': 'Hello', 'privacy_settings': {'last_seen': 'everyone'}})
	assert response.status_code == 200
	user = app.users['test@test.com']
	assert user.profile_picture == 'test.jpg'
	assert user.status_message == 'Hello'
	assert user.privacy_settings == {'last_seen': 'everyone'}

def test_send_message(client):
	client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	client.post('/register', json={'name': 'Test2', 'email': 'test2@test.com', 'password': 'test2'})
	response = client.post('/send_message', json={'from_user': 'test@test.com', 'to_user': 'test2@test.com', 'message': 'Hello'})
	assert response.status_code == 201
	assert isinstance(app.messages['test2@test.com'][0], Message)
	assert app.messages['test2@test.com'][0].message == 'Hello'

def test_get_messages(client):
	client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	client.post('/register', json={'name': 'Test2', 'email': 'test2@test.com', 'password': 'test2'})
	client.post('/send_message', json={'from_user': 'test@test.com', 'to_user': 'test2@test.com', 'message': 'Hello'})
	response = client.get('/get_messages', query_string={'to_user': 'test2@test.com'})
	assert response.status_code == 200
	assert response.get_json()[0]['read'] == True
