import user

def test_create_user():
	assert user.create_user('testuser', 'testpassword', 'testemail@test.com') == 'User created successfully'
	assert user.create_user('testuser', 'testpassword', 'testemail@test.com') == 'Username already exists'


def test_login():
	assert user.login('testuser', 'testpassword') == 'Login successful'
	assert user.login('testuser', 'wrongpassword') == 'Invalid username or password'
	assert user.login('wronguser', 'testpassword') == 'Invalid username or password'


def test_recover_password():
	assert user.recover_password('testuser') == 'Password recovery email sent'
	assert user.recover_password('wronguser') == 'Username does not exist'


def test_link_bank_account():
	assert user.link_bank_account('testuser', 'Test Bank', '123456', 1000) == 'Bank account linked successfully'
	assert user.link_bank_account('wronguser', 'Test Bank', '123456', 1000) == 'Username does not exist'


def test_import_transactions():
	transactions = [{'amount': 100, 'description': 'Groceries'}, {'amount': -50, 'description': 'Salary'}]
	assert user.import_transactions('testuser', '123456', transactions) == 'Transactions imported successfully'
	assert user.import_transactions('testuser', 'wrongaccount', transactions) == 'Username or account number does not exist'


def test_update_balance():
	assert user.update_balance('testuser', '123456', 950) == 'Balance updated successfully'
	assert user.update_balance('testuser', 'wrongaccount', 950) == 'Username or account number does not exist'
