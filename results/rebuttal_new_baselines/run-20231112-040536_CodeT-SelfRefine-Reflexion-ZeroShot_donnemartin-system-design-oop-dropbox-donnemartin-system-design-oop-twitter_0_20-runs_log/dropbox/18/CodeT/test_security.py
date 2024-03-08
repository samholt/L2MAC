import security

def test_get_activity_log():
	response, status_code = security.get_activity_log()
	assert status_code == 200
	assert isinstance(response, list)
