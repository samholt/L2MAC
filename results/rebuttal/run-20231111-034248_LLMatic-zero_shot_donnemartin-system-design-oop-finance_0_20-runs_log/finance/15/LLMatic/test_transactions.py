import transactions

def test_add_income():
	t = transactions.Transaction()
	t.add_income('user1', 1000, 'salary')
	assert t.get_transactions('user1') == [{'id': 0, 'type': 'income', 'amount': 1000, 'category': 'salary'}]

def test_add_expense():
	t = transactions.Transaction()
	t.add_expense('user1', 500, 'groceries')
	assert t.get_transactions('user1') == [{'id': 0, 'type': 'expense', 'amount': 500, 'category': 'groceries'}]

def test_categorize_transaction():
	t = transactions.Transaction()
	t.add_income('user1', 1000, 'salary')
	t.categorize_transaction('user1', 0, 'bonus')
	assert t.get_transactions('user1')[0]['category'] == 'bonus'
