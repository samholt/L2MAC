import pytest
import security

def test_encrypt_file():
	data = {'name': 'test.txt'}
	response, status_code = security.encrypt_file(data)
	assert status_code == 201
	assert response['message'] == 'File encrypted successfully'

def test_activity_log():
	data = {'user': 'test@example.com', 'action': 'upload', 'timestamp': '2022-01-01T00:00:00Z'}
	response, status_code = security.activity_log(data)
	assert status_code == 201
	assert response['message'] == 'Activity logged successfully'
