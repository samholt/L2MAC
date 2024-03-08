import pytest
import file_sharing

def test_generate_link():
	data = {'url': 'https://example.com', 'expiry_date': '2022-12-31', 'password': 'password'}
	response, status_code = file_sharing.generate_link(data)
	assert status_code == 201
	assert response['message'] == 'Link generated successfully'

def test_invite_user():
	data = {'email': 'test@example.com'}
	response, status_code = file_sharing.invite_user(data)
	assert status_code == 201
	assert response['message'] == 'User invited successfully'

def test_set_permission():
	data = {'email': 'test@example.com', 'permission': 'read'}
	response, status_code = file_sharing.set_permission(data)
	assert status_code == 201
	assert response['message'] == 'Permission set successfully'
