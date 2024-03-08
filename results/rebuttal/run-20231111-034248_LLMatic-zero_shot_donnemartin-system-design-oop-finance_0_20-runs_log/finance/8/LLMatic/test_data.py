import data

def test_add_transaction():
	data_obj = data.Data()
	transaction = data.Transaction('1', 'income', 1000, 'salary')
	data_obj.add_transaction(transaction)
	assert '1' in data_obj.transactions


def test_update_transaction():
	data_obj = data.Data()
	transaction = data.Transaction('1', 'income', 1000, 'salary')
	data_obj.add_transaction(transaction)
	data_obj.update_transaction('1', 'expense', 500, 'groceries')
	assert data_obj.transactions['1'].type == 'expense'
	assert data_obj.transactions['1'].amount == 500
	assert data_obj.transactions['1'].category == 'groceries'


def test_delete_transaction():
	data_obj = data.Data()
	transaction = data.Transaction('1', 'income', 1000, 'salary')
	data_obj.add_transaction(transaction)
	data_obj.delete_transaction('1')
	assert '1' not in data_obj.transactions


def test_categorize_transactions():
	data_obj = data.Data()
	transaction1 = data.Transaction('1', 'income', 1000, 'salary')
	transaction2 = data.Transaction('2', 'expense', 500, 'groceries')
	data_obj.add_transaction(transaction1)
	data_obj.add_transaction(transaction2)
	categories = data_obj.categorize_transactions()
	assert 'salary' in categories
	assert 'groceries' in categories
