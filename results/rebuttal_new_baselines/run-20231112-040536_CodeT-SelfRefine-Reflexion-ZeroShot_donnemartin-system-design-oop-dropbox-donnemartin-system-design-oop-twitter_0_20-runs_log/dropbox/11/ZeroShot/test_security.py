import pytest
import security

def test_encrypt_file():
	data = {'file_name': 'NewTest'}
	response = security.encrypt_file(data)
	assert response == {'message': 'File encrypted successfully'}

def test_activity_log():
	data = {'user_email': 'test@test.com', 'action': 'upload'}
	response = security.activity_log(data)
	assert response == {'message': 'Activity logged successfully'}
