import user

def test_create_user():
	assert user.create_user('test', 'password') == 'User created successfully'
	assert user.create_user('test', 'password') == 'Username already exists'

def test_login():
	assert user.login('test', 'password') == 'Login successful'
	assert user.login('test', 'wrong_password') == 'Invalid username or password'
	assert user.login('wrong_username', 'password') == 'Invalid username or password'

def test_recover_password():
	assert user.recover_password('test') == 'Password recovery email sent'
	assert user.recover_password('wrong_username') == 'Username does not exist'
