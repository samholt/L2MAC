import pytest
import security

def test_activity_log():
	data = {'user_email': 'test@test.com', 'action': 'login'}
	response = security.activity_log(data)
	assert response == {'message': 'Activity logged successfully'}
