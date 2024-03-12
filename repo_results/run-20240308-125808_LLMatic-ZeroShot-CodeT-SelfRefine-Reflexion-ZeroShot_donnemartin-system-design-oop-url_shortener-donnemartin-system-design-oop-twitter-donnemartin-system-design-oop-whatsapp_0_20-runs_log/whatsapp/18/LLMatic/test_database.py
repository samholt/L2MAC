import app


def test_add_user():
	app.DATABASE['users']['test_user'] = {
		'email': 'test@test.com',
		'password': 'test_password',
		'profile_picture': 'test_picture',
		'status_message': 'Hello, world!',
		'privacy_settings': 'public',
		'blocked_contacts': []
	}
	assert 'test_user' in app.DATABASE['users']


def test_retrieve_user():
	user = app.DATABASE['users'].get('test_user')
	assert user is not None


def test_update_user():
	app.DATABASE['users']['test_user']['status_message'] = 'Updated status'
	assert app.DATABASE['users']['test_user']['status_message'] == 'Updated status'


def test_delete_user():
	del app.DATABASE['users']['test_user']
	assert 'test_user' not in app.DATABASE['users']
