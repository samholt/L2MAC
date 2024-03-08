import users

def test_create_user():
	assert users.create_user('test_user', 'test_password') == 'User created successfully'
	assert users.create_user('test_user', 'test_password') == 'User already exists'

def test_get_user():
	assert users.get_user('test_user').username == 'test_user'
	assert users.get_user('non_existent_user') == 'User not found'

def test_create_profile():
	user = users.get_user('test_user')
	user.create_profile({'name': 'Test User', 'email': 'test_user@example.com'})
	assert user.profile == {'name': 'Test User', 'email': 'test_user@example.com'}

def test_customize_profile():
	user = users.get_user('test_user')
	user.customize_profile({'name': 'Updated User'})
	assert user.profile == {'name': 'Updated User', 'email': 'test_user@example.com'}

def test_save_event():
	user = users.get_user('test_user')
	user.save_event('Event 1', 'upcoming')
	assert user.get_events('upcoming') == ['Event 1']

