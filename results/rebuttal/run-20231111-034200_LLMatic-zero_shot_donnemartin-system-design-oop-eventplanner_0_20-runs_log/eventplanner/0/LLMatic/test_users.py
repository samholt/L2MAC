import users

def test_create_user():
	user = users.create_user('test', 'password')
	assert user.username == 'test'
	assert user.password == 'password'


def test_customize_profile():
	user = users.create_user('test', 'password')
	users.customize_profile(user, {'name': 'Test User', 'email': 'test@example.com'})
	assert user.profile == {'name': 'Test User', 'email': 'test@example.com'}


def test_save_event():
	user = users.create_user('test', 'password')
	users.save_event(user, 'Event 1', 'upcoming')
	assert user.events['upcoming'] == ['Event 1']


def test_get_events():
	user = users.create_user('test', 'password')
	users.save_event(user, 'Event 1', 'upcoming')
	assert users.get_events(user, 'upcoming') == ['Event 1']
