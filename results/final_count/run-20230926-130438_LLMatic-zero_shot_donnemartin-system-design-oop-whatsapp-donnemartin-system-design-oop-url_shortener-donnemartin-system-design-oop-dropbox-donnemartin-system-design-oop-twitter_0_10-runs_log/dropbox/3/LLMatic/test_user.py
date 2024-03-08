import user

def test_register():
	user.register('Test User', 'test@example.com', 'password')
	assert 'test@example.com' in user.mock_db
	assert user.mock_db['test@example.com'].name == 'Test User'

def test_login():
	user.register('Test User', 'test@example.com', 'password')
	assert user.login('test@example.com', 'password')

def test_forgot_password():
	user.register('Test User', 'test@example.com', 'password')
	user.forgot_password('test@example.com', 'new_password')
	assert user.login('test@example.com', 'new_password')

def test_profile():
	user.register('Test User', 'test@example.com', 'password')
	profile = user.profile('test@example.com')
	assert profile['name'] == 'Test User'
	assert profile['email'] == 'test@example.com'
	assert profile['profile_picture'] == 'default.jpg'
	assert profile['storage_used'] == 0
	assert profile['storage_remaining'] == 100

def test_change_password():
	user.register('Test User', 'test@example.com', 'password')
	user.change_password('test@example.com', 'new_password')
	assert user.login('test@example.com', 'new_password')
