import bank


def test_link_account():
	assert bank.link_account('user1', '1234567890') == 'Bank account linked successfully'
	assert bank.link_account('user1', '1234567890') == 'Bank account linked successfully'


def test_import_transactions():
	assert bank.import_transactions('user1', '1234567890') == 'Transactions imported successfully'
	assert bank.import_transactions('user1', '0987654321') == 'Invalid username or bank account number'


def test_update_account_balance():
	balance = bank.update_account_balance('user1', '1234567890')
	assert isinstance(balance, int)
	assert bank.update_account_balance('user1', '0987654321') == 'Invalid username or bank account number'
