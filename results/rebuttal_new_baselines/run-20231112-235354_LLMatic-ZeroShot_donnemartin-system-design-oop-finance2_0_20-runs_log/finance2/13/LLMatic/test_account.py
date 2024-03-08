import account

def test_user_creation():
	user = account.User('test_user', 'test_password')
	assert user.username == 'test_user'
	assert user.password == 'test_password'


def test_user_authentication():
	user = account.User('test_user', 'test_password')
	user.send_auth_code('test_email@test.com')
	assert user.authenticate_user('test_user', 'test_password', '123456') == True


def test_link_bank_account():
	user = account.User('test_user', 'test_password')
	user.link_bank_account('1234567890')
	assert '1234567890' in user.linked_bank_accounts
