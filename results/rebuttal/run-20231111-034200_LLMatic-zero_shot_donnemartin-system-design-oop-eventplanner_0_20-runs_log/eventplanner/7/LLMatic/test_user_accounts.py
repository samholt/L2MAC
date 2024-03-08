import user_accounts

def test_create_user():
	user_accounts.create_user('test', 'password')
	user = user_accounts.get_user('test')
	assert user is not None


def test_create_and_customize_profile():
	user_accounts.create_user('test', 'password')
	user = user_accounts.get_user('test')
	user.create_profile({'name': 'Test User', 'email': 'test@example.com'})
	assert user.profile == {'name': 'Test User', 'email': 'test@example.com'}
	user.customize_profile({'phone': '1234567890'})
	assert user.profile == {'name': 'Test User', 'email': 'test@example.com', 'phone': '1234567890'}


def test_save_and_get_events():
	user_accounts.create_user('test', 'password')
	user = user_accounts.get_user('test')
	user.save_event('Event 1')
	user.save_event('Event 2')
	assert user.get_events() == ['Event 1', 'Event 2']
