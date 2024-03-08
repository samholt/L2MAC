import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		# Create test users
		user_data1 = {
			'email': 'test@example.com',
			'password': 'password',
			'profile_picture': 'picture.jpg',
			'status_message': 'Hello!',
			'privacy_settings': 'public',
			'blocked_contacts': [],
			'groups': {},
			'messages': []
		}
		client.post('/users', json=user_data1)
		user_data2 = {
			'email': 'test2@example.com',
			'password': 'password',
			'profile_picture': 'picture.jpg',
			'status_message': 'Hello!',
			'privacy_settings': 'public',
			'blocked_contacts': [],
			'groups': {},
			'messages': []
		}
		client.post('/users', json=user_data2)
		yield client

def test_create_and_get_user(client):
	response = client.get('/users/test@example.com')
	assert response.status_code == 200

def test_recover_password(client):
	response = client.post('/users/test@example.com/recover')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password recovery email sent'}

	response = client.post('/users/nonexistent@example.com/recover')
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found'}

def test_set_profile_picture(client):
	response = client.post('/users/test@example.com/profile_picture', json={'profile_picture': 'new_picture.jpg'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile picture updated'}

	response = client.get('/users/test@example.com')
	assert response.status_code == 200
	assert response.get_json()['profile_picture'] == 'new_picture.jpg'

def test_set_status_message(client):
	response = client.post('/users/test@example.com/status_message', json={'status_message': 'New status message'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status message updated'}

	response = client.get('/users/test@example.com')
	assert response.status_code == 200
	assert response.get_json()['status_message'] == 'New status message'

def test_set_privacy_settings(client):
	response = client.post('/users/test@example.com/privacy_settings', json={'privacy_settings': 'private'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Privacy settings updated'}

	response = client.get('/users/test@example.com')
	assert response.status_code == 200
	assert response.get_json()['privacy_settings'] == 'private'

def test_block_and_unblock_contact(client):
	response = client.post('/users/test@example.com/block', json={'blocked_email': 'blocked@example.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact blocked'}

	response = client.get('/users/test@example.com')
	assert response.status_code == 200
	assert 'blocked@example.com' in response.get_json()['blocked_contacts']

	response = client.post('/users/test@example.com/unblock', json={'unblocked_email': 'blocked@example.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact unblocked'}

	response = client.get('/users/test@example.com')
	assert response.status_code == 200
	assert 'blocked@example.com' not in response.get_json()['blocked_contacts']

def test_manage_groups(client):
	response = client.post('/users/test@example.com/groups', json={'group_name': 'Friends', 'contacts': ['friend1@example.com', 'friend2@example.com']})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Group updated'}

	response = client.get('/users/test@example.com')
	assert response.status_code == 200
	assert 'Friends' in response.get_json()['groups']
	assert response.get_json()['groups']['Friends'] == ['friend1@example.com', 'friend2@example.com']

def test_send_and_read_message(client):
	message_data = {'sender_email': 'test@example.com', 'receiver_email': 'test2@example.com', 'message': 'Hello!'}
	response = client.post('/message/send', json=message_data)
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message sent'}

	response = client.get('/users/test@example.com')
	assert response.status_code == 200
	assert response.get_json()['messages'][0]['message'] == 'Hello!'
	assert response.get_json()['messages'][0]['read'] == False

	response = client.post('/message/read', json=message_data)
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message marked as read'}

	response = client.get('/users/test@example.com')
	assert response.status_code == 200
	assert response.get_json()['messages'][0]['read'] == True

def test_encrypt_message(client):
	response = client.post('/message/encrypt', json={'message': 'Hello!'})
	assert response.status_code == 200
	assert response.get_json()['encrypted_message'] == '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

def test_share_image(client):
	image_data = {'sender_email': 'test@example.com', 'receiver_email': 'test2@example.com', 'image': 'image.jpg'}
	response = client.post('/message/share_image', json=image_data)
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Image shared'}

	response = client.get('/users/test@example.com')
	assert response.status_code == 200
	assert response.get_json()['messages'][1]['image'] == 'image.jpg'

