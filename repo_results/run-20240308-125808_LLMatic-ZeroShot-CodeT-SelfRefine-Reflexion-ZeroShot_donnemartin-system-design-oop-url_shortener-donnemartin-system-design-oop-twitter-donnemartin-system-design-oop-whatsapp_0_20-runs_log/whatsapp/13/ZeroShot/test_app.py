import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', data=json.dumps({'email': 'test@test.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_login(client):
	client.post('/register', data=json.dumps({'email': 'test@test.com', 'password': 'password'}), content_type='application/json')
	response = client.post('/login', data=json.dumps({'email': 'test@test.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert 'id' in response.get_json()


def test_create_chat(client):
	response = client.post('/chat', data=json.dumps({'name': 'Test Chat'}), content_type='application/json')
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_send_message(client):
	chat_response = client.post('/chat', data=json.dumps({'name': 'Test Chat'}), content_type='application/json')
	chat_id = chat_response.get_json()['id']
	response = client.post(f'/chat/{chat_id}/message', data=json.dumps({'user_id': '1', 'content': 'Hello, world!'}), content_type='application/json')
	assert response.status_code == 201
	assert 'id' in response.get_json()
