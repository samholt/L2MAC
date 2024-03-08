import pytest
import security

def test_get_activity_log():
	response, status_code = security.get_activity_log()
	assert status_code == 200
	assert 'activity_log' in response
