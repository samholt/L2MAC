import pytest
import app

@pytest.fixture

def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'email': 'test@test.com', 'password': 'test', 'profile_picture': 'test.jpg', 'status_message': 'Hello, world!', 'privacy_settings': 'public'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}


def test_get_user(client):
	response = client.get('/user/test@test.com')
	assert response.status_code == 200
	assert response.get_json() == {'email': 'test@test.com', 'password': 'test', 'profile_picture': 'test.jpg', 'status_message': 'Hello, world!', 'privacy_settings': 'public'}


def test_recover_password(client):
	response = client.get('/user/test@test.com/recover')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password recovery email sent'}


def test_set_profile_picture(client):
	response = client.post('/user/test@test.com/profile_picture', json={'profile_picture': 'new_test.jpg'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile picture updated'}
	user = app.users_db.get('test@test.com')
	assert user['profile_picture'] == 'new_test.jpg'


def test_set_status_message(client):
	response = client.post('/user/test@test.com/status_message', json={'status_message': 'New status message'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status message updated'}
	user = app.users_db.get('test@test.com')
	assert user['status_message'] == 'New status message'


def test_set_privacy_settings(client):
	response = client.post('/user/test@test.com/privacy_settings', json={'privacy_settings': 'private'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Privacy settings updated'}
	user = app.users_db.get('test@test.com')
	assert user['privacy_settings'] == 'private'


def test_block_contact(client):
	response = client.post('/user/test@test.com/block', json={'contact_email': 'block@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact blocked'}
	user = app.users_db.get('test@test.com')
	assert 'block@test.com' in user['blocked_contacts']


def test_unblock_contact(client):
	response = client.post('/user/test@test.com/unblock', json={'contact_email': 'block@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact unblocked'}
	user = app.users_db.get('test@test.com')
	assert 'block@test.com' not in user['blocked_contacts']


def test_manage_group(client):
	response = client.post('/user/test@test.com/group', json={'group_name': 'Test Group', 'group_members': ['member1@test.com', 'member2@test.com']})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Group updated'}
	user = app.users_db.get('test@test.com')
	assert 'Test Group' in user['groups']
	assert user['groups']['Test Group'] == ['member1@test.com', 'member2@test.com']
