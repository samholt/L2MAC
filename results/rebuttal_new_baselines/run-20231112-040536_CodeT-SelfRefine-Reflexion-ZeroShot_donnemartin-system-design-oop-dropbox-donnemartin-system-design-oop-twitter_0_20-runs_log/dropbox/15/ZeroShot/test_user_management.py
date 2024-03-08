import user_management

def test_register():
	data = {'name': 'Test', 'email': 'test@example.com', 'password': 'test', 'profile_picture': '', 'storage_used': 0, 'storage_remaining': 1000}
	response = user_management.register(data)
	assert response['status'] == 'success'

def test_login():
	data = {'email': 'test@example.com', 'password': 'test'}
	response = user_management.login(data)
	assert response['status'] == 'success'

def test_forgot_password():
	data = {'email': 'test@example.com', 'new_password': 'new_test'}
	response = user_management.forgot_password(data)
	assert response['status'] == 'success'

def test_get_profile():
	data = {'email': 'test@example.com'}
	response = user_management.get_profile(data)
	assert 'name' in response

def test_update_profile():
	data = {'email': 'test@example.com', 'name': 'New Test'}
	response = user_management.update_profile(data)
	assert response['status'] == 'success'
