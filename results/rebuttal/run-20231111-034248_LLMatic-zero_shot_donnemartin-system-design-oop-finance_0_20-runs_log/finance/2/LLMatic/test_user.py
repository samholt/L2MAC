import user


def test_create_user():
	assert user.create_user('test', 'password')
	assert not user.create_user('test', 'password')


def test_login():
	assert not user.login('test', 'wrong_password')
	assert user.login('test', 'password')


def test_recover_password():
	assert user.recover_password('test') == user.User('test', 'password').password
	assert user.recover_password('non_existent') is None
