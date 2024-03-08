import user_management

def test_register_user():
	# Test with valid data
	assert user_management.register_user('John Doe', 'john.doe@example.com', 'password123') == True
	assert 'john.doe@example.com' in user_management.users_db

	# Test with invalid email
	assert user_management.register_user('John Doe', 'john.doe', 'password123') == False

	# Test with weak password
	assert user_management.register_user('John Doe', 'john.doe@example.com', 'password') == False

def test_authenticate_user():
	# Test with valid data
	user_management.register_user('Jane Doe', 'jane.doe@example.com', 'password123')
	assert user_management.authenticate_user('jane.doe@example.com', 'password123') == 'Login successful'

	# Test with invalid email
	assert user_management.authenticate_user('jane.doe', 'password123') == 'Login failed'

	# Test with incorrect password
	assert user_management.authenticate_user('jane.doe@example.com', 'password') == 'Login failed'
