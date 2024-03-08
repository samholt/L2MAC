import pytest
import security

def test_encrypt_file():
	data = {'file_name': 'Test'}
	response = security.encrypt_file(data)
	assert response['status'] == 'success'

def test_activity_log():
	data = {'user_email': 'test@test.com', 'action': 'upload'}
	response = security.activity_log(data)
	assert response['status'] == 'success'
