import pytest
from app import app, users_db, messages_db
import base64

@pytest.fixture

def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Welcome to the Home Page!'


def test_register(client):
	response = client.post('/register', json={
		'email': 'test@example.com',
		'password': 'password123'
	})
	assert response.status_code == 200
	assert response.data == b'User registered successfully!'
	assert 'test@example.com' in users_db
	assert users_db['test@example.com']['password'] == 'password123'


def test_login(client):
	# Test successful login
	client.post('/register', json={'email': 'test2@example.com', 'password': 'password123'})
	response = client.post('/login', json={'email': 'test2@example.com', 'password': 'password123'})
	assert response.status_code == 200
	assert response.data == b'Logged in successfully!'
	# Test failed login
	response = client.post('/login', json={'email': 'nonexistent@example.com', 'password': 'password123'})
	assert response.status_code == 401
	assert response.data == b'Invalid email or password!'


def test_recover_password(client):
	# Test password recovery for existing user
	client.post('/register', json={'email': 'test3@example.com', 'password': 'password123'})
	response = client.post('/recover_password', json={'email': 'test3@example.com'})
	assert response.status_code == 200
	assert response.data == b'https://example.com/reset_password/test3@example.com'
	# Test password recovery for non-existing user
	response = client.post('/recover_password', json={'email': 'nonexistent@example.com'})
	assert response.status_code == 404
	assert response.data == b'No user with this email!'


def test_update_profile(client):
	# Test profile update for existing user
	client.post('/register', json={'email': 'test4@example.com', 'password': 'password123'})
	response = client.post('/update_profile', json={'email': 'test4@example.com', 'profile_picture': 'new_picture.jpg', 'status_message': 'Hello, world!', 'privacy_settings': 'private'})
	assert response.status_code == 200
	assert response.data == b'Profile updated successfully!'
	user = users_db['test4@example.com']
	assert user['profile_picture'] == 'new_picture.jpg'
	assert user['status_message'] == 'Hello, world!'
	assert user['privacy_settings'] == 'private'
	# Test profile update for non-existing user
	response = client.post('/update_profile', json={'email': 'nonexistent@example.com'})
	assert response.status_code == 404
	assert response.data == b'No user with this email!'


def test_block_unblock_contact(client):
	# Test blocking a contact
	client.post('/register', json={'email': 'test5@example.com', 'password': 'password123'})
	response = client.post('/block_contact', json={'email': 'test5@example.com', 'contact_email': 'contact@example.com'})
	assert response.status_code == 200
	assert response.data == b'Contact blocked successfully!'
	user = users_db['test5@example.com']
	assert 'contact@example.com' in user['blocked_contacts']
	# Test unblocking a contact
	response = client.post('/unblock_contact', json={'email': 'test5@example.com', 'contact_email': 'contact@example.com'})
	assert response.status_code == 200
	assert response.data == b'Contact unblocked successfully!'
	user = users_db['test5@example.com']
	assert 'contact@example.com' not in user['blocked_contacts']


def test_group_management(client):
	# Test creating a group
	client.post('/register', json={'email': 'test6@example.com', 'password': 'password123'})
	response = client.post('/create_group', json={'email': 'test6@example.com', 'group_name': 'Friends', 'group_picture': 'group.jpg'})
	assert response.status_code == 200
	assert response.data == b'Group created successfully!'
	user = users_db['test6@example.com']
	assert 'Friends' in user['groups']
	group = user['groups']['Friends']
	assert group['group_picture'] == 'group.jpg'
	assert group['participants'] == []
	assert group['admins'] == ['test6@example.com']
	# Test editing a group
	response = client.post('/edit_group', json={'email': 'test6@example.com', 'group_name': 'Friends', 'group_picture': 'new_group.jpg', 'add_participants': ['friend1@example.com', 'friend2@example.com'], 'remove_participants': [], 'add_admins': ['friend1@example.com'], 'remove_admins': []})
	assert response.status_code == 200
	assert response.data == b'Group edited successfully!'
	group = user['groups']['Friends']
	assert group['group_picture'] == 'new_group.jpg'
	assert 'friend1@example.com' in group['participants']
	assert 'friend2@example.com' in group['participants']
	assert 'friend1@example.com' in group['admins']
	response = client.post('/edit_group', json={'email': 'test6@example.com', 'group_name': 'Friends', 'add_participants': [], 'remove_participants': ['friend1@example.com'], 'add_admins': [], 'remove_admins': ['friend1@example.com']})
	assert response.status_code == 200
	assert response.data == b'Group edited successfully!'
	group = user['groups']['Friends']
	assert 'friend1@example.com' not in group['participants']
	assert 'friend2@example.com' in group['participants']
	assert 'friend1@example.com' not in group['admins']


def test_send_receive_messages(client):
	# Test sending a message
	client.post('/register', json={'email': 'test7@example.com', 'password': 'password123'})
	client.post('/register', json={'email': 'test8@example.com', 'password': 'password123'})
	response = client.post('/send_message', json={'sender_email': 'test7@example.com', 'recipient_email': 'test8@example.com', 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert response.data == b'Message sent successfully!'
	message = messages_db[0]
	assert message['sender'] == 'test7@example.com'
	assert message['recipient'] == 'test8@example.com'
	assert message['content'] == base64.b64encode('Hello, world!'.encode()).decode()
	assert message['read'] == False
	# Test receiving messages
	response = client.get('/receive_messages', query_string={'email': 'test8@example.com'})
	assert response.status_code == 200
	messages = response.get_json()['messages']
	assert len(messages) == 1
	message = messages[0]
	assert message['sender'] == 'test7@example.com'
	assert message['recipient'] == 'test8@example.com'
	assert message['content'] == 'Hello, world!'
	assert message['read'] == False
	# Test marking a message as read
	response = client.post('/mark_as_read', json={'message_id': 0})
	assert response.status_code == 200
	assert response.data == b'Message marked as read!'
	message = messages_db[0]
	assert message['read'] == True


def test_send_media(client):
	# Test sending media
	client.post('/register', json={'email': 'test9@example.com', 'password': 'password123'})
	client.post('/register', json={'email': 'test10@example.com', 'password': 'password123'})
	response = client.post('/send_media', json={'sender_email': 'test9@example.com', 'recipient_email': 'test10@example.com', 'media_content': 'image.jpg'})
	assert response.status_code == 200
	assert response.data == b'Media sent successfully!'
	message = messages_db[1]
	assert message['sender'] == 'test9@example.com'
	assert message['recipient'] == 'test10@example.com'
	assert message['content'] == 'image.jpg'
	assert message['read'] == False
