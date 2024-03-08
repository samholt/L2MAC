import user


def test_user_creation():
	user1 = user.User('test_user', 'test_password')
	assert user1.username == 'test_user'
	assert user1.check_password('test_password')


def test_password_change():
	user1 = user.User('test_user', 'test_password')
	user1.change_password('new_password')
	assert user1.check_password('new_password')


def test_password_recovery():
	user1 = user.User('test_user', 'test_password')
	assert user1.recover_password() == 'Recovery link has been sent to your email.'
