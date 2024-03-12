import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}

	response = client.post('/user', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}


def test_get_user(client):
	client.post('/user', json={'email': 'test@test.com', 'password': 'test'})
	response = client.get('/user/test@test.com')
	assert response.status_code == 200
	assert response.get_json() == {'email': 'test@test.com', 'password': 'test'}


def test_reset_password(client):
	client.post('/user', json={'email': 'test@test.com', 'password': 'test'})
	response = client.post('/user/test@test.com/reset_password', json={'new_password': 'new_test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password reset successful'}

	response = client.get('/user/test@test.com')
	assert response.status_code == 200
	assert response.get_json() == {'email': 'test@test.com', 'password': 'new_test'}


def test_set_profile_picture(client):
	client.post('/user', json={'email': 'test@test.com', 'password': 'test'})
	response = client.post('/user/test@test.com/profile_picture', json={'profile_picture': 'new_picture.jpg'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile picture set'}


def test_set_status_message(client):
	client.post('/user', json={'email': 'test@test.com', 'password': 'test'})
	response = client.post('/user/test@test.com/status_message', json={'status_message': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status message set'}


def test_update_privacy_settings(client):
	client.post('/user', json={'email': 'test@test.com', 'password': 'test'})
	response = client.post('/user/test@test.com/privacy_settings', json={'privacy_settings': {'last_seen': 'friends', 'profile_picture': 'everyone', 'status_message': 'no_one'}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Privacy settings updated'}


def test_block_contact(client):
	client.post('/user', json={'email': 'test@test.com', 'password': 'test', 'blocked_contacts': []})
	response = client.post('/user/test@test.com/block', json={'contact_email': 'block@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact blocked'}


def test_unblock_contact(client):
	client.post('/user', json={'email': 'test@test.com', 'password': 'test', 'blocked_contacts': ['block@test.com']})
	response = client.post('/user/test@test.com/unblock', json={'contact_email': 'block@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact unblocked'}


def test_create_group(client):
	response = client.post('/group', json={'name': 'Test Group', 'members': ['test@test.com']})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Group created', 'group_id': 1}


def test_get_group(client):
	client.post('/group', json={'name': 'Test Group', 'members': ['test@test.com']})
	response = client.get('/group/1')
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Test Group', 'members': ['test@test.com']}


def test_edit_group(client):
	client.post('/group', json={'name': 'Test Group', 'members': ['test@test.com']})
	response = client.post('/group/1/edit', json={'name': 'New Test Group', 'members': ['new_test@test.com']})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Group updated'}

