import pytest
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_create_group(client):
	response = client.post('/groups', json={'email': 'admin@test.com', 'group_name': 'Test Group', 'participants': ['user1@test.com', 'user2@test.com']})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Group created'}


def test_add_participant(client):
	response = client.post('/groups/Test Group/participants', json={'participant_email': 'user3@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Participant added'}


def test_remove_participant(client):
	response = client.delete('/groups/Test Group/participants', json={'participant_email': 'user2@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Participant removed'}


def test_manage_admin(client):
	response = client.post('/groups/Test Group/admin', json={'admin_email': 'newadmin@test.com', 'permissions': ['add', 'remove']})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Admin roles updated'}
