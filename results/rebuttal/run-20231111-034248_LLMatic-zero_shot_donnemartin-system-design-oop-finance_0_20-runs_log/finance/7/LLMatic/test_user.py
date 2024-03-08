import user

def test_create_user():
	assert user.create_user('testuser', 'testpassword', 'testemail@test.com') == 'User created successfully'
	assert user.create_user('testuser', 'testpassword', 'testemail@test.com') == 'Username already exists'

def test_login_logout():
	assert user.login('testuser', 'wrongpassword') == 'Invalid username or password'
	assert user.login('testuser', 'testpassword') == 'Logged in successfully'
	assert user.logout('testuser') == 'Logged out successfully'

def test_recover_password():
	assert user.recover_password('wronguser') == 'Invalid username'
	assert user.recover_password('testuser') == 'Password recovery email has been sent to testemail@test.com'
