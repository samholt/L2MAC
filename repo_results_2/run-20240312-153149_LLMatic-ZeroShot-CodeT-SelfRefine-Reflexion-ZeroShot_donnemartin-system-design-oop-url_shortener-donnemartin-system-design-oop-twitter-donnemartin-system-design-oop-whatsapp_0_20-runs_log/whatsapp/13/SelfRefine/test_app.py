import pytest
import app
import user
import chat

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_login(client):
	client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 200
	assert 'id' in response.get_json()


def test_forgot_password(client):
	client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	response = client.post('/forgot_password', json={'email': 'test@test.com'})
	assert response.status_code == 200


def test_update_profile(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	user_id = response.get_json()['id']
	response = client.post('/update_profile', json={'user_id': user_id, 'profile_picture': 'picture.jpg', 'status_message': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json()['profile_picture'] == 'picture.jpg'
	assert response.get_json()['status_message'] == 'Hello, world!'


def test_block_user(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	user_id = response.get_json()['id']
	response = client.post('/block_user', json={'user_id': user_id, 'blocked_user_id': '123'})
	assert response.status_code == 200


def test_unblock_user(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	user_id = response.get_json()['id']
	client.post('/block_user', json={'user_id': user_id, 'blocked_user_id': '123'})
	response = client.post('/unblock_user', json={'user_id': user_id, 'unblocked_user_id': '123'})
	assert response.status_code == 200


def test_create_group(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	admin_id = response.get_json()['id']
	response = client.post('/create_group', json={'name': 'Test Group', 'picture': 'group.jpg', 'admin_id': admin_id})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_add_participant(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	admin_id = response.get_json()['id']
	response = client.post('/create_group', json={'name': 'Test Group', 'picture': 'group.jpg', 'admin_id': admin_id})
	chat_id = response.get_json()['id']
	response = client.post('/add_participant', json={'chat_id': chat_id, 'participant_id': '123'})
	assert response.status_code == 200
	assert '123' in response.get_json()['participants']


def test_remove_participant(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	admin_id = response.get_json()['id']
	response = client.post('/create_group', json={'name': 'Test Group', 'picture': 'group.jpg', 'admin_id': admin_id})
	chat_id = response.get_json()['id']
	client.post('/add_participant', json={'chat_id': chat_id, 'participant_id': '123'})
	response = client.post('/remove_participant', json={'chat_id': chat_id, 'participant_id': '123'})
	assert response.status_code == 200
	assert '123' not in response.get_json()['participants']
