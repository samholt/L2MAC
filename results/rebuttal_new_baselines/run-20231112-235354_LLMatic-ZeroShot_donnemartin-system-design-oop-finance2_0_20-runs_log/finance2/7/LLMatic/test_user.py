import user

def test_user_creation():
	user_obj = user.User('test_user', 'test_password')
	assert user_obj.username == 'test_user'
	assert user_obj.password == 'test_password'

def test_user_update():
	user_obj = user.User('test_user', 'test_password')
	user_obj.update_user('updated_user', 'updated_password')
	assert user_obj.username == 'updated_user'
	assert user_obj.password == 'updated_password'

def test_user_deletion():
	user_obj = user.User('test_user', 'test_password')
	user_obj.delete_user()
	assert user_obj.username == None
	assert user_obj.password == None
	assert user_obj.bank_accounts == []

def test_link_bank_account():
	user_obj = user.User('test_user', 'test_password')
	user_obj.link_bank_account('1234567890')
	assert '1234567890' in user_obj.bank_accounts
