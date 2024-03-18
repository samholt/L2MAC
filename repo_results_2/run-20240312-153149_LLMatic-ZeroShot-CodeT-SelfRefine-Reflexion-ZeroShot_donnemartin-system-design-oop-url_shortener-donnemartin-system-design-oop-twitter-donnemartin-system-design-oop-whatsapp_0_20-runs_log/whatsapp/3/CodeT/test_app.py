import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'User registered successfully'

	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data)['message'] == 'Email already registered'

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Logged in successfully'

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrong'})
	assert response.status_code == 400
	assert json.loads(response.data)['message'] == 'Invalid email or password'

	response = client.post('/forgot_password', json={'email': 'test@test.com', 'new_password': 'new'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Password updated successfully'

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'new'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Logged in successfully'

	response = client.post('/update_profile', json={'email': 'test@test.com', 'profile': {'picture': 'pic.jpg', 'status': 'Hello'}})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Profile updated successfully'

	response = client.post('/block_contact', json={'email': 'test@test.com', 'contact': 'contact@test.com'})
	assert response.status_code == 400
	assert json.loads(response.data)['message'] == 'Contact not found'

	response = client.post('/unblock_contact', json={'email': 'test@test.com', 'contact': 'contact@test.com'})
	assert response.status_code == 400
	assert json.loads(response.data)['message'] == 'Contact not blocked'

	response = client.post('/create_group', json={'email': 'test@test.com', 'name': 'Test Group', 'picture': 'group.jpg'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Group created successfully'

	response = client.post('/send_message', json={'email': 'test@test.com', 'receiver': 'receiver@test.com', 'message': 'Hello'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Message sent successfully'

	response = client.post('/read_message', json={'message_id': 1})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Message marked as read'

	response = client.post('/post_status', json={'email': 'test@test.com', 'status': 'Hello', 'visibility': 'public'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Status posted successfully'
