import user


def test_link_bank_account():
	user.create_user('test_user', 'test_password', 'test_email')
	assert user.link_bank_account('test_user', 'test_bank', '123456', 1000) == 'Bank account linked successfully'
	assert user.link_bank_account('non_existent_user', 'test_bank', '123456', 1000) == 'Username does not exist'


def test_import_transactions():
	user.create_user('test_user2', 'test_password', 'test_email')
	user.link_bank_account('test_user2', 'test_bank', '123456', 1000)
	transactions = [{'amount': 100, 'description': 'Groceries'}, {'amount': -50, 'description': 'Salary'}]
	assert user.import_transactions('test_user2', '123456', transactions) == 'Transactions imported successfully'
	assert user.import_transactions('non_existent_user', '123456', transactions) == 'Username or account number does not exist'


def test_update_account_balance():
	user.create_user('test_user3', 'test_password', 'test_email')
	user.link_bank_account('test_user3', 'test_bank', '123456', 1000)
	assert user.update_account_balance('test_user3', '123456', 500) == 'Account balance updated successfully'
	assert user.update_account_balance('non_existent_user', '123456', 500) == 'Username or account number does not exist'
