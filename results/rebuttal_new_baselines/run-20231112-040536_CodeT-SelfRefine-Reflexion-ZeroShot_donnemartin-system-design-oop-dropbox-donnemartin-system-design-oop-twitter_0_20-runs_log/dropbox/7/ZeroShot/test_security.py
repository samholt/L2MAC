import pytest
import security

def test_activity_log():
	data = {'user_email': 'test@test.com', 'action': 'Test Action'}
	response = security.activity_log(data)
	assert response == {'message': 'Activity logged successfully'}
