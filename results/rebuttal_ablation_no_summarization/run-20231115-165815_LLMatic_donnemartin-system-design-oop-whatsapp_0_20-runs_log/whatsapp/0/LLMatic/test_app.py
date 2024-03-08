import pytest
import app
import json


def test_register():
	response = app.app.test_client().post('/register', data=json.dumps({'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'


def test_recover_password():
	response = app.app.test_client().post('/recover_password', data=json.dumps({'email': 'test@test.com', 'recovery': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Password recovery set'


def test_set_profile_picture():
	response = app.app.test_client().post('/set_profile_picture', data=json.dumps({'email': 'test@test.com', 'picture': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Profile picture set'


def test_set_status_message():
	response = app.app.test_client().post('/set_status_message', data=json.dumps({'email': 'test@test.com', 'message': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Status message set'


def test_update_privacy_settings():
	response = app.app.test_client().post('/update_privacy_settings', data=json.dumps({'email': 'test@test.com', 'details': 'private', 'last_seen': 'private'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Privacy settings updated'


def test_block_contact():
	response = app.app.test_client().post('/block_contact', data=json.dumps({'email': 'test@test.com', 'contact': 'test2@test.com'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Contact blocked successfully'


def test_unblock_contact():
	response = app.app.test_client().post('/unblock_contact', data=json.dumps({'email': 'test@test.com', 'contact': 'test2@test.com'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Contact unblocked successfully'


def test_create_group():
	response = app.app.test_client().post('/create_group', data=json.dumps({'group_name': 'test', 'admin': 'test@test.com', 'picture': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Group created successfully'


def test_add_member():
	response = app.app.test_client().post('/add_member', data=json.dumps({'group_name': 'test', 'member': 'test2@test.com'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Member added successfully'


def test_remove_member():
	response = app.app.test_client().post('/remove_member', data=json.dumps({'group_name': 'test', 'member': 'test2@test.com'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Member removed successfully'


def test_block_member():
	response = app.app.test_client().post('/block_member', data=json.dumps({'group_name': 'test', 'member': 'test2@test.com'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Member blocked successfully'


def test_unblock_member():
	response = app.app.test_client().post('/unblock_member', data=json.dumps({'group_name': 'test', 'member': 'test2@test.com'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Member unblocked successfully'
