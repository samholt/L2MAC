import user

def test_create_user():
	assert user.create_user('testuser', 'testpassword', 'testemail@test.com') == 'User created successfully'
	assert user.create_user('testuser', 'testpassword', 'testemail@test.com') == 'Username already exists'

def test_login():
	assert user.login('testuser', 'testpassword') == 'Login successful'
	assert user.login('testuser', 'wrongpassword') == 'Invalid username or password'
	assert user.login('wronguser', 'testpassword') == 'Invalid username or password'

def test_recover_password():
	assert user.recover_password('testuser') == 'Password recovery email sent'
	assert user.recover_password('wronguser') == 'Username does not exist'
