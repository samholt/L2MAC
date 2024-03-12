import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

# Test user registration
@pytest.mark.parametrize('email, password', [('test@test.com', 'password'), ('test2@test.com', 'password')])
def test_register(client, email, password):
	response = client.post('/register', json={'email': email, 'password': password})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Registration successful'

# Test user login
@pytest.mark.parametrize('email, password', [('test@test.com', 'password'), ('test2@test.com', 'password')])
def test_login(client, email, password):
	response = client.post('/login', json={'email': email, 'password': password})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Login successful'

# Test password reset
@pytest.mark.parametrize('email, new_password', [('test@test.com', 'new_password'), ('test2@test.com', 'new_password')])
def test_forgot_password(client, email, new_password):
	response = client.post('/forgot_password', json={'email': email, 'new_password': new_password})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Password reset successful'

# Test set profile
@pytest.mark.parametrize('email, profile', [('test@test.com', {'picture': 'picture.jpg', 'status': 'Hello, world!'}), ('test2@test.com', {'picture': 'picture2.jpg', 'status': 'Hello, world 2!'})])
def test_set_profile(client, email, profile):
	response = client.post('/set_profile', json={'email': email, 'profile': profile})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Profile set successful'

# Test add contact
@pytest.mark.parametrize('email, contact', [('test@test.com', 'test2@test.com')])
def test_add_contact(client, email, contact):
	response = client.post('/add_contact', json={'email': email, 'contact': contact})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Contact added'

# Test block contact
@pytest.mark.parametrize('email, contact', [('test@test.com', 'test2@test.com')])
def test_block_contact(client, email, contact):
	response = client.post('/block_contact', json={'email': email, 'contact': contact})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Contact blocked'

# Test unblock contact
@pytest.mark.parametrize('email, contact', [('test@test.com', 'test2@test.com')])
def test_unblock_contact(client, email, contact):
	response = client.post('/unblock_contact', json={'email': email, 'contact': contact})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Contact unblocked'

# Test create group
@pytest.mark.parametrize('email, name, picture', [('test@test.com', 'Group', 'group.jpg')])
def test_create_group(client, email, name, picture):
	response = client.post('/create_group', json={'email': email, 'name': name, 'picture': picture})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Group created'

# Test send message
@pytest.mark.parametrize('email, receiver, message', [('test@test.com', 'receiver@test.com', 'Hello, world!')])
def test_send_message(client, email, receiver, message):
	response = client.post('/send_message', json={'email': email, 'receiver': receiver, 'message': message})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Message sent'

# Test read message
@pytest.mark.parametrize('message_id', [1])
def test_read_message(client, message_id):
	response = client.post('/read_message', json={'message_id': message_id})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Message marked as read'

# Test post status
@pytest.mark.parametrize('email, status, visibility', [('test@test.com', 'Hello, world!', 'public')])
def test_post_status(client, email, status, visibility):
	response = client.post('/post_status', json={'email': email, 'status': status, 'visibility': visibility})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Status posted'
