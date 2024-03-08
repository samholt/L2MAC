import pytest
import file_sharing

def test_share_file():
	data = {'file_name': 'NewTest', 'user_email': 'test@test.com', 'permissions': 'read'}
	response = file_sharing.share_file(data)
	assert response == {'message': 'File shared successfully'}

def test_invite_user():
	data = {'file_name': 'NewTest', 'user_email': 'new_test@test.com'}
	response = file_sharing.invite_user(data)
	assert response == {'message': 'User invited successfully'}
