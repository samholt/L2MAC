import pytest
import json
from app import app, users, groups, statuses, messages

@pytest.fixture

def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_create_group(client):
	users['test@test.com'] = {}
	response = client.post('/create_group', json={'email': 'test@test.com', 'group_name': 'Test Group', 'picture': '', 'participants': ['participant@test.com']})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'Group created'}
	assert 'Test Group' in groups


def test_add_participant(client):
	users['test@test.com'] = {}
	users['participant@test.com'] = {}
	groups['Test Group'] = {'admin': 'test@test.com', 'picture': '', 'participants': ['test@test.com'], 'admins': ['test@test.com']}
	response = client.post('/add_participant', json={'email': 'test@test.com', 'group_name': 'Test Group', 'participant_email': 'participant@test.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'Participant added'}
	assert 'participant@test.com' in groups['Test Group']['participants']


def test_remove_participant(client):
	users['test@test.com'] = {}
	users['participant@test.com'] = {}
	groups['Test Group'] = {'admin': 'test@test.com', 'picture': '', 'participants': ['test@test.com', 'participant@test.com'], 'admins': ['test@test.com']}
	response = client.post('/remove_participant', json={'email': 'test@test.com', 'group_name': 'Test Group', 'participant_email': 'participant@test.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'Participant removed'}
	assert 'participant@test.com' not in groups['Test Group']['participants']


def test_manage_admins(client):
	users['test@test.com'] = {}
	users['admin@test.com'] = {}
	groups['Test Group'] = {'admin': 'test@test.com', 'picture': '', 'participants': ['test@test.com'], 'admins': ['test@test.com']}
	response = client.post('/manage_admins', json={'email': 'test@test.com', 'group_name': 'Test Group', 'admins': ['admin@test.com']})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'Admins updated'}
	assert 'admin@test.com' in groups['Test Group']['admins']


def test_post_status(client):
	users['test@test.com'] = {}
	response = client.post('/post_status', json={'email': 'test@test.com', 'image': 'image.jpg', 'timestamp': '2022-01-01T00:00:00Z'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'Status posted'}
	assert 'test@test.com' in statuses


def test_update_status_visibility(client):
	users['test@test.com'] = {}
	statuses['test@test.com'] = {'image': 'image.jpg', 'timestamp': '2022-01-01T00:00:00Z', 'visible_to': []}
	response = client.post('/update_status_visibility', json={'email': 'test@test.com', 'status': 'test@test.com', 'contacts': ['contact@test.com']})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'Status visibility updated'}
	assert 'contact@test.com' in statuses['test@test.com']['visible_to']


def test_update_online_status(client):
	users['test@test.com'] = {'online': 'offline'}
	messages['test@test.com'] = ['Hello, world!']
	response = client.post('/update_online_status', json={'email': 'test@test.com', 'status': 'online'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'Online status updated'}
	assert users['test@test.com']['online'] == 'online'
	assert messages['test@test.com'] == []

