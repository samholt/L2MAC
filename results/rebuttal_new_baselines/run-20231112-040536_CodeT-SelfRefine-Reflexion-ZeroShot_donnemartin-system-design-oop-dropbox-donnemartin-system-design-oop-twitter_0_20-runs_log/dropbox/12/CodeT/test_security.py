import pytest
import security

def test_log_activity():
	security.log_activity('Test activity')
	assert len(security.get_activity_log()) == 1

def test_get_activity_log():
	response, status_code = security.get_activity_log()
	assert status_code == 200
	assert len(response) == 1
