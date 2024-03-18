import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_and_get_user(client):
	user_data = {
		'email': 'test@example.com',
		'password': 'password',
		'profile_picture': 'picture.jpg',
		'status_message': 'Hello!',
		'privacy_settings': 'public'
	}
	response = client.post('/user', json=user_data)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}

	response = client.get(f'/user/{user_data["email"]}')
	assert response.status_code == 200
	assert response.get_json() == user_data


def test_signup(client):
	response = client.post('/signup', json={'email': 'signup@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered'}

	response = client.post('/signup', json={'email': 'signup@example.com', 'password': 'password'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Email already registered'}


def test_recover_password(client):
	response = client.post('/recover_password', json={'email': 'signup@example.com'})
	assert response.status_code == 200
	assert 'new_password' in response.get_json()
	assert response.get_json()['new_password'] == 'new_password'

	response = client.post('/recover_password', json={'email': 'nonexistent@example.com'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found'}


def test_profile_management(client):
	user_data = {
		'email': 'test@example.com',
		'password': 'password',
		'profile_picture': 'picture.jpg',
		'status_message': 'Hello!',
		'privacy_settings': 'public'
	}
	client.post('/user', json=user_data)

	response = client.post(f'/user/{user_data["email"]}/profile_picture', json={'profile_picture': 'new_picture.jpg'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile picture updated'}

	response = client.post(f'/user/{user_data["email"]}/status_message', json={'status_message': 'New status'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status message updated'}

	response = client.post(f'/user/{user_data["email"]}/privacy_settings', json={'privacy_settings': 'private'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Privacy settings updated'}

	response = client.get(f'/user/{user_data["email"]}')
	assert response.status_code == 200
	assert response.get_json()['profile_picture'] == 'new_picture.jpg'
	assert response.get_json()['status_message'] == 'New status'
	assert response.get_json()['privacy_settings'] == 'private'


def test_contact_management(client):
	user_data = {
		'email': 'test@example.com',
		'password': 'password',
		'profile_picture': 'picture.jpg',
		'status_message': 'Hello!',
		'privacy_settings': 'public'
	}
	client.post('/user', json=user_data)

	response = client.post(f'/user/{user_data["email"]}/block', json={'blocked_contact': 'block@example.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact blocked'}

	response = client.post(f'/user/{user_data["email"]}/unblock', json={'unblocked_contact': 'block@example.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact unblocked'}


def test_group_management(client):
	group_data = {
		'name': 'Test Group',
		'picture': 'group.jpg',
		'members': ['test@example.com']
	}
	response = client.post('/group', json=group_data)
	assert response.status_code == 201
	assert 'group_id' in response.get_json()
	group_id = response.get_json()['group_id']

	response = client.get(f'/group/{group_id}')
	assert response.status_code == 200
	assert response.get_json() == group_data

	response = client.post(f'/group/{group_id}/add_member', json={'member': 'new@example.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Member added'}

	response = client.post(f'/group/{group_id}/remove_member', json={'member': 'new@example.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Member removed'}

	response = client.post(f'/group/{group_id}/set_details', json={'name': 'New Group', 'picture': 'new_group.jpg'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Group details updated'}


def test_message_management(client):
	message_data = {
		'sender': 'test@example.com',
		'receiver': 'receiver@example.com',
		'message': 'Hello!'
	}
	response = client.post('/message', json=message_data)
	assert response.status_code == 201
	assert 'message_id' in response.get_json()
	message_id = response.get_json()['message_id']

	response = client.get(f'/message/{message_id}')
	assert response.status_code == 200
	assert response.get_json()['sender'] == message_data['sender']
	assert response.get_json()['receiver'] == message_data['receiver']
	assert response.get_json()['message'] == message_data['message']

	response = client.post(f'/message/{message_id}/read')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message marked as read'}

	response = client.get(f'/message/{message_id}')
	assert response.status_code == 200
	assert response.get_json()['read'] == True

	response = client.post(f'/message/{message_id}/encrypt')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message encrypted'}

	response = client.get(f'/message/{message_id}')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'encrypted_' + message_data['message']

