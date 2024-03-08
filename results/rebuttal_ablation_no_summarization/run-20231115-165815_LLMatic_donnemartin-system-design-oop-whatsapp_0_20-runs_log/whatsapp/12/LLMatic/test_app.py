import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'email': 'test@test.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}


def test_update_online_status(client):
	client.post('/user', json={'email': 'test@test.com'})
	response = client.put('/user/test@test.com/online', json={'online': False})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Online status updated'}
	user = app.users_db['test@test.com']
	assert user['online'] == False


def test_send_message_offline(client):
	client.post('/user', json={'email': 'test@test.com'})
	client.put('/user/test@test.com/online', json={'online': False})
	response = client.post('/user/test@test.com/message', json={'id': '1', 'content': 'Hello'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message queued'}
	user = app.users_db['test@test.com']
	assert user['message_queue'] == [{'id': '1', 'content': 'Hello', 'read': False}]


def test_send_message_online(client):
	client.post('/user', json={'email': 'test@test.com'})
	response = client.post('/user/test@test.com/message', json={'id': '1', 'content': 'Hello'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message sent'}
	user = app.users_db['test@test.com']
	assert user['messages'] == [{'id': '1', 'content': 'Hello', 'read': False}]


def test_go_online(client):
	client.post('/user', json={'email': 'test@test.com'})
	client.put('/user/test@test.com/online', json={'online': False})
	client.post('/user/test@test.com/message', json={'id': '1', 'content': 'Hello'})
	response = client.put('/user/test@test.com/online', json={'online': True})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Online status updated'}
	user = app.users_db['test@test.com']
	assert user['messages'] == [{'id': '1', 'content': 'Hello', 'read': False}]
	assert user['message_queue'] == []
