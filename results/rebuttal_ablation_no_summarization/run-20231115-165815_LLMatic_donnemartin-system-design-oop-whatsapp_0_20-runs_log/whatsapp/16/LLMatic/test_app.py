import pytest
from app import app, users, groups, statuses, messages
import time

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', data={'email': 'test@test.com', 'name': 'Test User'})
	assert response.status_code == 201
	user_id = response.get_json()['user_id']
	assert users[user_id] == {'email': 'test@test.com', 'name': 'Test User', 'online': False}
	assert messages[user_id] == []


def test_create_group(client):
	response = client.post('/create_group', data={'name': 'Test Group', 'picture': 'test.jpg'})
	assert response.status_code == 201
	group_id = response.get_json()['group_id']
	assert groups[group_id] == {'name': 'Test Group', 'picture': 'test.jpg', 'participants': [], 'admins': []}


def test_add_participant(client):
	user_response = client.post('/create_user', data={'email': 'test@test.com', 'name': 'Test User'})
	user_id = user_response.get_json()['user_id']
	group_response = client.post('/create_group', data={'name': 'Test Group', 'picture': 'test.jpg'})
	group_id = group_response.get_json()['group_id']
	response = client.post('/add_participant', data={'group_id': group_id, 'user_id': user_id})
	assert response.status_code == 200
	assert user_id in groups[group_id]['participants']


def test_remove_participant(client):
	user_response = client.post('/create_user', data={'email': 'test@test.com', 'name': 'Test User'})
	user_id = user_response.get_json()['user_id']
	group_response = client.post('/create_group', data={'name': 'Test Group', 'picture': 'test.jpg'})
	group_id = group_response.get_json()['group_id']
	client.post('/add_participant', data={'group_id': group_id, 'user_id': user_id})
	response = client.post('/remove_participant', data={'group_id': group_id, 'user_id': user_id})
	assert response.status_code == 200
	assert user_id not in groups[group_id]['participants']


def test_update_admin(client):
	user_response = client.post('/create_user', data={'email': 'test@test.com', 'name': 'Test User'})
	user_id = user_response.get_json()['user_id']
	group_response = client.post('/create_group', data={'name': 'Test Group', 'picture': 'test.jpg'})
	group_id = group_response.get_json()['group_id']
	client.post('/add_participant', data={'group_id': group_id, 'user_id': user_id})
	response = client.post('/update_admin', data={'group_id': group_id, 'user_id': user_id})
	assert response.status_code == 200
	assert user_id in groups[group_id]['admins']


def test_post_status(client):
	user_response = client.post('/create_user', data={'email': 'test@test.com', 'name': 'Test User'})
	user_id = user_response.get_json()['user_id']
	response = client.post('/post_status', data={'user_id': user_id, 'image': 'test.jpg', 'visibility': 'public'})
	assert response.status_code == 201
	status_id = response.get_json()['status_id']
	assert statuses[status_id]['user_id'] == user_id
	assert statuses[status_id]['image'] == 'test.jpg'
	assert statuses[status_id]['visibility'] == 'public'


def test_send_message(client):
	from_user_response = client.post('/create_user', data={'email': 'from@test.com', 'name': 'From User'})
	from_user_id = from_user_response.get_json()['user_id']
	to_user_response = client.post('/create_user', data={'email': 'to@test.com', 'name': 'To User'})
	to_user_id = to_user_response.get_json()['user_id']
	response = client.post('/send_message', data={'from_user_id': from_user_id, 'to_user_id': to_user_id, 'message': 'Hello'})
	assert response.status_code == 200
	assert messages[to_user_id] == [{'from': from_user_id, 'message': 'Hello'}]


def test_check_online_status(client):
	user_response = client.post('/create_user', data={'email': 'test@test.com', 'name': 'Test User'})
	user_id = user_response.get_json()['user_id']
	response = client.get('/check_online_status', query_string={'user_id': user_id})
	assert response.status_code == 200
	assert response.get_json()['online'] == False


def test_update_online_status(client):
	user_response = client.post('/create_user', data={'email': 'test@test.com', 'name': 'Test User'})
	user_id = user_response.get_json()['user_id']
	response = client.post('/update_online_status', data={'user_id': user_id, 'online': 'True'})
	assert response.status_code == 200
	assert users[user_id]['online'] == True
	assert response.get_json()['message'] == 'Online status updated'

