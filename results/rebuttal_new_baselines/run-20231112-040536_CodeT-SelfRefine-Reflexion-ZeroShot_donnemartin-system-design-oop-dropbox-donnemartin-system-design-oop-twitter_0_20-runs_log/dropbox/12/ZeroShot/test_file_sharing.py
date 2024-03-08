import pytest
import file_sharing

def test_share_file():
	data = {'file_name': 'Test', 'user_email': 'test@test.com', 'permissions': ['read']}
	response = file_sharing.share_file(data)
	assert response['status'] == 'success'

def test_invite_user():
	data = {'file_name': 'Test', 'user_email': 'new_test@test.com'}
	response = file_sharing.invite_user(data)
	assert response['status'] == 'success'
