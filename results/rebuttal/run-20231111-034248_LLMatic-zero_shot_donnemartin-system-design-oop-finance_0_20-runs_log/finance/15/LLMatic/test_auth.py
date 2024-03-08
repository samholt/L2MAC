import auth

def test_register_user():
	assert auth.register_user('test_user', 'test_password') == True
	assert auth.register_user('test_user', 'test_password') == False


def test_login_user():
	assert auth.login_user('test_user', 'test_password') == True
	assert auth.login_user('test_user', 'wrong_password') == False
	assert auth.login_user('wrong_user', 'test_password') == False


def test_logout_user():
	assert auth.logout_user('test_user') == True
	assert auth.logout_user('wrong_user') == False


def test_recover_password():
	assert auth.recover_password('test_user') == True
	assert auth.recover_password('wrong_user') == False
