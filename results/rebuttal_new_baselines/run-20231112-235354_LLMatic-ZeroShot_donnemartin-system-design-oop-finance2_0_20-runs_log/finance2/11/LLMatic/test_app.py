from account import User

def test_create_account():
	user = User()
	assert user.create_account('test', 'password') == 'Account created successfully'
	assert user.create_account('test', 'password') == 'Username already exists'

def test_link_bank_account():
	user = User()
	user.create_account('test', 'password')
	assert user.link_bank_account('test', '123456') == 'Bank account linked successfully'
	assert user.link_bank_account('test', '123456') == 'Bank account already linked to another user'
	user2 = User()
	user2.create_account('nonexistent', 'password')
	assert user2.link_bank_account('nonexistent', '123456') == 'Bank account linked successfully'

def test_handle_authentication():
	user = User()
	user.create_account('test', 'password')
	assert user.handle_authentication('test', 'password') == 'Authentication successful'
	assert user.handle_authentication('test', 'wrongpassword') == 'Authentication failed'
	assert user.handle_authentication('nonexistent', 'password') == 'Authentication failed'
