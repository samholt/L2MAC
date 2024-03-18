import pytest
from mock_db import MockDB
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_create_group(client):
	response = client.post('/create-group', json={'email': 'test@example.com', 'group_name': 'Test Group', 'members': ['member1@example.com', 'member2@example.com']})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Group created successfully'


def test_edit_group(client):
	response = client.post('/edit-group', json={'email': 'test@example.com', 'group_name': 'Test Group', 'members': ['member1@example.com', 'member3@example.com']})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Group edited successfully'


def test_add_group_admin(client):
	response = client.post('/add-group-admin', json={'email': 'test@example.com', 'group_name': 'Test Group', 'admin_email': 'member1@example.com'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Admin added successfully'


def test_remove_group_admin(client):
	response = client.post('/remove-group-admin', json={'email': 'test@example.com', 'group_name': 'Test Group', 'admin_email': 'member1@example.com'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Admin removed successfully'
