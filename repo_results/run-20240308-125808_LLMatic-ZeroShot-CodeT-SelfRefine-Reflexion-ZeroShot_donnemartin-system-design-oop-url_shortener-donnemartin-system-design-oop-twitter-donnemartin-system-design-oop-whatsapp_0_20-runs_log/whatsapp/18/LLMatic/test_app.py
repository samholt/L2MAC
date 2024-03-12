import pytest
import app


def test_signup():
	with app.app.test_client() as client:
		response = client.post('/signup', json={'email': 'test@test.com', 'password': 'test123'})
		assert response.get_json()['message'] == 'User registered successfully'


def test_login():
	with app.app.test_client() as client:
		response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
		assert response.get_json()['message'] == 'User logged in successfully'
		assert app.DATABASE['users']['test@test.com']['online'] == True


def test_logout():
	with app.app.test_client() as client:
		response = client.post('/logout', json={'email': 'test@test.com'})
		assert response.get_json()['message'] == 'User logged out successfully'
		assert app.DATABASE['users']['test@test.com']['online'] == False


def test_send_message():
	with app.app.test_client() as client:
		response = client.post('/signup', json={'email': 'test2@test.com', 'password': 'test123'})
		response = client.post('/send_message', json={'sender': 'test@test.com', 'receiver': 'test2@test.com', 'message': 'Hello', 'image_url': ''})
		assert response.status_code == 200
		assert 'message_id' in response.get_json()


def test_receive_message():
	with app.app.test_client() as client:
		response = client.post('/signup', json={'email': 'test3@test.com', 'password': 'test123'})
		response = client.post('/send_message', json={'sender': 'test@test.com', 'receiver': 'test3@test.com', 'message': 'Hello', 'image_url': ''})
		assert len(app.DATABASE['messages']) > 0 or len(app.DATABASE['offline_messages']) > 0
		message_id = list(app.DATABASE['messages'].keys())[0] if len(app.DATABASE['messages']) > 0 else list(app.DATABASE['offline_messages'].keys())[0]
		response = client.post('/receive_message', json={'message_id': message_id})
		if message_id in app.DATABASE['messages']:
			assert response.status_code == 200
			assert 'message' in response.get_json()
		else:
			assert response.status_code == 404


def test_read_receipt():
	with app.app.test_client() as client:
		response = client.post('/signup', json={'email': 'test4@test.com', 'password': 'test123'})
		response = client.post('/send_message', json={'sender': 'test@test.com', 'receiver': 'test4@test.com', 'message': 'Hello', 'image_url': ''})
		assert len(app.DATABASE['messages']) > 0 or len(app.DATABASE['offline_messages']) > 0
		message_id = list(app.DATABASE['messages'].keys())[0] if len(app.DATABASE['messages']) > 0 else list(app.DATABASE['offline_messages'].keys())[0]
		response = client.post('/read_receipt', json={'message_id': message_id})
		if message_id in app.DATABASE['messages']:
			assert response.get_json()['message'] == 'Read receipt sent'
			assert app.DATABASE['messages'][message_id]['read'] == True
		else:
			assert response.status_code == 404


def test_offline_message():
	with app.app.test_client() as client:
		client.post('/logout', json={'email': 'test@test.com'})
		response = client.post('/send_message', json={'sender': 'test2@test.com', 'receiver': 'test@test.com', 'message': 'Hello', 'image_url': ''})
		assert response.status_code == 200
		assert 'message_id' in response.get_json()
		assert len(app.DATABASE['offline_messages']) > 0
		client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
		assert len(app.DATABASE['offline_messages']) == 0
		assert len(app.DATABASE['messages']) > 0
