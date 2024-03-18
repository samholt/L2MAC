import pytest
import app
import mock_db

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def setup_module(module):
	app.db.add_user('test_user', 'test_password')
	app.db.create_group('test_user', {'name': 'Test Group', 'picture': 'test_picture.jpg'})
	app.db.add_participant(1, 'test_participant')
	app.db.add_admin(1, 'test_admin')


def test_create_group(client):
	response = client.post('/create_group', json={'user_id': 'test_user', 'group_details': {'name': 'Test Group', 'picture': 'test_picture.jpg'}})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Group created successfully'


def test_edit_group(client):
	response = client.post('/edit_group', json={'user_id': 'test_user', 'group_id': 1, 'group_details': {'name': 'Edited Test Group', 'picture': 'edited_test_picture.jpg'}})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Group edited successfully'


def test_delete_group(client):
	response = client.post('/delete_group', json={'user_id': 'test_user', 'group_id': 1})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Group deleted successfully'


def test_add_participant(client):
	response = client.post('/add_participant', json={'group_id': 1, 'participant_id': 'test_participant'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Participant added successfully'


def test_remove_participant(client):
	response = client.post('/remove_participant', json={'group_id': 1, 'participant_id': 'test_participant'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Participant removed successfully'


def test_add_admin(client):
	response = client.post('/add_admin', json={'group_id': 1, 'admin_id': 'test_admin'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Admin added successfully'


def test_remove_admin(client):
	response = client.post('/remove_admin', json={'group_id': 1, 'admin_id': 'test_admin'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Admin removed successfully'


