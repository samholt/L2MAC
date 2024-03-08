import pytest
import security

def test_get_activity():
	response, status_code = security.get_activity()
	assert status_code == 200
	assert len(response) == 0
