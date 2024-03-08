import pytest
import security

def test_log_activity():
	activity = 'User test@test.com uploaded file.txt'
	response, status_code = security.log_activity(activity)
	assert status_code == 201
	assert response['message'] == 'Activity logged successfully'

def test_get_activity_log():
	response, status_code = security.get_activity_log()
	assert status_code == 200
	assert len(response) == 1
