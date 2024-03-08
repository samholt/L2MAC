import user_accounts


def test_create_account():
	assert user_accounts.create_account('test', 'password') == {'result': True}
	assert user_accounts.create_account('test', 'password') == {'result': False}


def test_add_url_to_account():
	assert user_accounts.add_url_to_account('test', 'short_url') == {'result': True}
	assert user_accounts.add_url_to_account('nonexistent', 'short_url') == {'result': False}


def test_remove_url_from_account():
	assert user_accounts.remove_url_from_account('test', 'short_url') == {'result': True}
	assert user_accounts.remove_url_from_account('test', 'nonexistent') == {'result': False}


def test_get_user_urls():
	assert user_accounts.get_user_urls('test') == {'result': []}
	assert user_accounts.get_user_urls('nonexistent') == {'result': False}


def test_authenticate_user():
	assert user_accounts.authenticate_user('test', 'password') == {'result': True}
	assert user_accounts.authenticate_user('test', 'wrong_password') == {'result': False}
	assert user_accounts.authenticate_user('nonexistent', 'password') == {'result': False}
