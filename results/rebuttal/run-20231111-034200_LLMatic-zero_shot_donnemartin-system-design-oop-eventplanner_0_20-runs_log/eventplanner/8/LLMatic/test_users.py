from users import User

def test_user_creation():
	user = User('test_user', 'test_password', 'test_profile')
	assert user.username == 'test_user'
	assert user.password == 'test_password'
	assert user.profile == 'test_profile'


def test_customize_profile():
	user = User('test_user', 'test_password', 'test_profile')
	user.customize_profile('new_profile')
	assert user.profile == 'new_profile'


def test_save_and_get_events():
	user = User('test_user', 'test_password', 'test_profile')
	user.save_event('test_event')
	assert user.get_events() == ['test_event']

