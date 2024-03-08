import user_accounts

def test_import():
	assert user_accounts is not None

def test_user_creation():
	user = user_accounts.User('test_user', 'password')
	assert user is not None

def test_profile_creation():
	user = user_accounts.User('test_user', 'password')
	user.create_profile({'name': 'Test User', 'email': 'test@example.com'})
	assert user.profile == {'name': 'Test User', 'email': 'test@example.com'}

def test_profile_customization():
	user = user_accounts.User('test_user', 'password')
	user.create_profile({'name': 'Test User', 'email': 'test@example.com'})
	user.customize_profile({'name': 'Updated User'})
	assert user.profile == {'name': 'Updated User', 'email': 'test@example.com'}

def test_event_saving():
	user = user_accounts.User('test_user', 'password')
	user.save_event('Event 1', 'upcoming')
	assert user.get_events('upcoming') == ['Event 1']

def test_event_accessing():
	user = user_accounts.User('test_user', 'password')
	user.save_event('Event 1', 'upcoming')
	assert user.get_events('upcoming') == ['Event 1']
