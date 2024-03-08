import security

def test_get_activity():
	data = {'user_email': 'test@example.com'}
	response = security.get_activity(data)
	assert 'activity' in response
