import security

def test_hash_password():
	assert len(security.hash_password('password')) == 192


def test_verify_password():
	stored_password = security.hash_password('password')
	assert security.verify_password(stored_password, 'password')


def test_store_user_data():
	security.store_user_data('user1', 'password')
	assert 'user1' in security.user_data


def test_check_user_data():
	security.store_user_data('user1', 'password')
	assert security.check_user_data('user1', 'password')
