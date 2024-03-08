import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

# Test user registration
@pytest.mark.parametrize('email, password', [('test@test.com', 'password')])
def test_register(client, email, password):
	response = client.post('/register', json={'email': email, 'password': password})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'User registered successfully'

# Test user login
@pytest.mark.parametrize('email, password', [('test@test.com', 'password')])
def test_login(client, email, password):
	response = client.post('/login', json={'email': email, 'password': password})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Logged in successfully'

# Test forgot password
@pytest.mark.parametrize('email, new_password', [('test@test.com', 'new_password')])
def test_forgot_password(client, email, new_password):
	response = client.post('/forgot_password', json={'email': email, 'new_password': new_password})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Password updated successfully'

# Test update profile
@pytest.mark.parametrize('email, profile', [('test@test.com', {'picture': 'picture.jpg', 'status': 'Hello, world!'})])
def test_update_profile(client, email, profile):
	response = client.post('/update_profile', json={'email': email, 'profile': profile})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Profile updated successfully'

# Test block contact
@pytest.mark.parametrize('email, contact', [('test@test.com', 'contact@test.com')])
def test_block_contact(client, email, contact):
	# Add the contact before blocking
	app.users[email]['contacts'].append(contact)
	response = client.post('/block_contact', json={'email': email, 'contact': contact})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Contact blocked successfully'

# Test create group
@pytest.mark.parametrize('email, name', [('test@test.com', 'Test Group')])
def test_create_group(client, email, name):
	response = client.post('/create_group', json={'email': email, 'name': name})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Group created successfully'

# Test send message
@pytest.mark.parametrize('sender, receiver, content', [('test@test.com', 'receiver@test.com', 'Hello, world!')])
def test_send_message(client, sender, receiver, content):
	# Add the receiver to the sender's contacts before sending the message
	app.users[sender]['contacts'].append(receiver)
	response = client.post('/send_message', json={'sender': sender, 'receiver': receiver, 'content': content})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Message sent successfully'
