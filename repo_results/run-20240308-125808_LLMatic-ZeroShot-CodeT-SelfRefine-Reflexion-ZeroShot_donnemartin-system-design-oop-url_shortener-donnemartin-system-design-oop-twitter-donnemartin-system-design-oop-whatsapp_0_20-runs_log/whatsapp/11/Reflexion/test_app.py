import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}


def test_create_chat(client):
	response = client.post('/create_chat', json={'users': ['test@test.com']})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Chat created successfully'}


def test_send_message(client):
	response = client.post('/send_message', json={'chat_id': 0, 'email': 'test@test.com', 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message sent successfully'}
