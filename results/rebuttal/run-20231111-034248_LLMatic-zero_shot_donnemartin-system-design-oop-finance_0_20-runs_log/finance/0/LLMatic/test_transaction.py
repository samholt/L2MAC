import transaction


def test_add_transaction():
	transaction.transactions_db = {}
	assert transaction.add_transaction('user1', 100, 'groceries') == 'Transaction added successfully'
	assert len(transaction.transactions_db['user1']) == 1
	assert transaction.transactions_db['user1'][0]['amount'] == 100
	assert transaction.transactions_db['user1'][0]['category'] == 'groceries'


def test_categorize_transaction():
	transaction.transactions_db = {'user1': [{'date': None, 'amount': 100, 'category': 'groceries', 'recurring': False}]}
	assert transaction.categorize_transaction('user1', 0, 'entertainment') == 'Transaction categorized successfully'
	assert transaction.transactions_db['user1'][0]['category'] == 'entertainment'


def test_identify_recurring_transactions():
	transaction.transactions_db = {'user1': [
		{'date': None, 'amount': 100, 'category': 'groceries', 'recurring': False},
		{'date': None, 'amount': 100, 'category': 'groceries', 'recurring': False}
	]}
	assert transaction.identify_recurring_transactions('user1') == 'Recurring transactions identified'
	assert transaction.transactions_db['user1'][0]['recurring']
	assert transaction.transactions_db['user1'][1]['recurring']
