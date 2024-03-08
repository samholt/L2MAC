import bank_accounts


def test_link_account():
	ba = bank_accounts.BankAccount()
	ba.link_account('123', {'name': 'Test Account', 'balance': 1000})
	assert '123' in ba.accounts


def test_import_transactions():
	ba = bank_accounts.BankAccount()
	ba.link_account('123', {'name': 'Test Account', 'balance': 1000})
	assert ba.import_transactions('123') == 'Transactions imported'


def test_get_balance():
	ba = bank_accounts.BankAccount()
	ba.link_account('123', {'name': 'Test Account', 'balance': 1000})
	assert ba.get_balance('123') == 'Account balance: 1000'


def test_get_transactions():
	ba = bank_accounts.BankAccount()
	ba.link_account('123', {'name': 'Test Account', 'balance': 1000})
	assert ba.get_transactions('123') == 'Transactions: []'

