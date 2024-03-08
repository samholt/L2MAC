import transaction


def test_add_transaction():
	assert transaction.add_transaction('test_user', 100, 'income', False)
	assert transaction.add_transaction('test_user', -50, 'expense', True)


def test_get_transactions():
	transactions = transaction.get_transactions('test_user')
	assert transactions is not None
	assert len(transactions) == 2
	assert transactions[0].amount == 100
	assert transactions[0].category == 'income'
	assert not transactions[0].recurring
	assert transactions[1].amount == -50
	assert transactions[1].category == 'expense'
	assert transactions[1].recurring


def test_get_recurring_transactions():
	transactions = transaction.get_recurring_transactions('test_user')
	assert transactions is not None
	assert len(transactions) == 1
	assert transactions[0].amount == -50
	assert transactions[0].category == 'expense'
	assert transactions[0].recurring
