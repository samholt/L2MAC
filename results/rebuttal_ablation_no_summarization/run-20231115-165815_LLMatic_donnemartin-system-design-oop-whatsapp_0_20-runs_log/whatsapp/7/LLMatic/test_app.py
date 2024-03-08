import pytest
import app
from flask import json
import hashlib

def test_home():
	response = app.home()
	assert response == 'Hello, World!'

def test_database():
	# Test that we can add and retrieve data from the mock database
	app.DATABASE['users']['1'] = {'name': 'Test User'}
	assert app.DATABASE['users']['1'] == {'name': 'Test User'}

def test_register():
	# Test user registration
	with app.app.test_client() as client:
		response = client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'User registered successfully'
		assert 'test@example.com' in app.DATABASE['users']
		assert app.DATABASE['users']['test@example.com']['password'] == 'password'

def test_forgot_password():
	# Test password recovery
	with app.app.test_client() as client:
		response = client.post('/forgot_password', json={'email': 'test@example.com'})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['recovery_link'] == 'http://example.com/recover?email=test@example.com'

def test_set_profile_picture():
	# Test setting profile picture
	with app.app.test_client() as client:
		response = client.post('/set_profile_picture', json={'user_id': '1', 'new_picture': 'new_picture.jpg'})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Profile picture updated successfully'
		assert app.DATABASE['profile_pictures']['1'] == 'new_picture.jpg'

def test_set_status_message():
	# Test setting status message
	with app.app.test_client() as client:
		response = client.post('/set_status_message', json={'user_id': '1', 'new_message': 'Hello, world!'})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Status message updated successfully'
		assert app.DATABASE['statuses']['1'] == 'Hello, world!'

def test_update_privacy_settings():
	# Test updating privacy settings
	with app.app.test_client() as client:
		response = client.post('/update_privacy_settings', json={'user_id': '1', 'new_settings': {'show_email': False, 'show_status': True}})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Privacy settings updated successfully'
		assert app.DATABASE['privacy_settings']['1'] == {'show_email': False, 'show_status': True}

def test_block_contact():
	# Test blocking a contact
	with app.app.test_client() as client:
		response = client.post('/block_contact', json={'user_id': '1', 'contact_id': '2'})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Contact blocked successfully'
		assert '2' in app.DATABASE['blocked_contacts']['1']

def test_unblock_contact():
	# Test unblocking a contact
	with app.app.test_client() as client:
		response = client.post('/unblock_contact', json={'user_id': '1', 'contact_id': '2'})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Contact unblocked successfully'
		assert '2' not in app.DATABASE['blocked_contacts']['1']

def test_create_group():
	# Test creating a group
	with app.app.test_client() as client:
		response = client.post('/create_group', json={'group_id': '1', 'group_data': {'name': 'Test Group', 'members': ['1', '2', '3']}})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Group created successfully'
		assert app.DATABASE['groups']['1'] == {'name': 'Test Group', 'members': ['1', '2', '3']}

def test_edit_group():
	# Test editing a group
	with app.app.test_client() as client:
		response = client.post('/edit_group', json={'group_id': '1', 'group_data': {'name': 'Edited Group', 'members': ['1', '2']}})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Group edited successfully'
		assert app.DATABASE['groups']['1'] == {'name': 'Edited Group', 'members': ['1', '2']}

def test_add_participant():
	# Test adding a participant to a group
	with app.app.test_client() as client:
		response = client.post('/add_participant', json={'group_id': '1', 'participant_id': '4'})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Participant added successfully'
		assert '4' in app.DATABASE['groups']['1']['participants']

def test_remove_participant():
	# Test removing a participant from a group
	with app.app.test_client() as client:
		response = client.post('/remove_participant', json={'group_id': '1', 'participant_id': '2'})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Participant removed successfully'
		assert '2' not in app.DATABASE['groups']['1']['participants']

def test_manage_admin():
	# Test managing admin roles and permissions
	with app.app.test_client() as client:
		response = client.post('/manage_admin', json={'group_id': '1', 'admin_data': {'admin_id': '1', 'permissions': ['add', 'remove']}})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Admin roles and permissions updated successfully'
		assert app.DATABASE['groups']['1']['admin'] == {'admin_id': '1', 'permissions': ['add', 'remove']}

def test_send_message():
	# Test sending a message
	with app.app.test_client() as client:
		response = client.post('/send_message', json={'message_id': '1', 'message': 'Hello, world!'})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Message sent successfully'
		assert app.DATABASE['messages']['1'] == 'Hello, world!'

def test_read_receipt():
	# Test updating read receipt
	with app.app.test_client() as client:
		response = client.post('/read_receipt', json={'message_id': '1'})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Read receipt updated successfully'
		assert app.DATABASE['read_receipts']['1'] == True

def test_encrypt_message():
	# Test encrypting a message
	with app.app.test_client() as client:
		message = 'Hello, world!'
		response = client.post('/encrypt_message', json={'message': message})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['encrypted_message'] == hashlib.sha256(message.encode()).hexdigest()

def test_share_image():
	# Test sharing an image
	with app.app.test_client() as client:
		response = client.post('/share_image', json={'image_id': '1', 'image': 'image.jpg'})
		data = json.loads(response.data)
		assert response.status_code == 200
		assert data['message'] == 'Image shared successfully'
		assert app.DATABASE['images']['1'] == 'image.jpg'
