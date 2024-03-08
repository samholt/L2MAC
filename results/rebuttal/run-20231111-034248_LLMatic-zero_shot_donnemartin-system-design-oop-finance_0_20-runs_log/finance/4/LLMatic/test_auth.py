import auth


def test_hash_password():
	assert auth.hash_password('password') == auth.hash_password('password')
	assert auth.hash_password('password') != auth.hash_password('different_password')


def test_login_logout():
	auth.users_db['test_user'] = {'password': auth.hash_password('password'), 'logged_in': False}
	assert auth.login('test_user', 'password')
	assert auth.is_authenticated('test_user')
	auth.logout('test_user')
	assert not auth.is_authenticated('test_user')


def test_non_existent_user():
	assert not auth.login('non_existent_user', 'password')
	assert not auth.is_authenticated('non_existent_user')
	assert not auth.logout('non_existent_user')
