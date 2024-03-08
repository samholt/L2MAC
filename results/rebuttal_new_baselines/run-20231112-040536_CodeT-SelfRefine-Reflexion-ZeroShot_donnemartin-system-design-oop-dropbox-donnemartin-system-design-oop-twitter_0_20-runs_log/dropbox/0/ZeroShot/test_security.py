import pytest
import security

def test_encryption():
	data = {'file': 'New Test File'}
	response = security.encryption(data)
	assert response == {'message': 'File encrypted successfully'}

def test_activity_log():
	data = {'user': 'test@example.com', 'action': 'Uploaded a file'}
	response = security.activity_log(data)
	assert response == {'message': 'Activity logged successfully'}
