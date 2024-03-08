import auth

def test_register_login_logout():
	# Register a new user
	assert auth.register_user('testuser', 'testpassword', 'testuser@example.com')
	
	# Attempt to register the same user again
	assert not auth.register_user('testuser', 'testpassword', 'testuser@example.com')
	
	# Log in the user
	assert auth.login_user('testuser', 'testpassword')
	
	# Attempt to log in with incorrect password
	assert not auth.login_user('testuser', 'wrongpassword')
	
	# Log out the user
	assert auth.logout_user('testuser') == 'testuser logged out.'
	
	# Attempt to log out a non-existent user
	assert auth.logout_user('nonexistentuser') == 'User not found.'
