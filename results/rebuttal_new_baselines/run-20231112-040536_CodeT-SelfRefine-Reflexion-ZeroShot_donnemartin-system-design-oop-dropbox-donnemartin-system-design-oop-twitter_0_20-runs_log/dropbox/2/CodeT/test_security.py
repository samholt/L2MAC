import pytest
import security

def test_log_activity():
	security.log_activity('Test activity')
	response, status_code = security.get_activity_log()
	assert status_code == 200
	assert 'Test activity' in response
