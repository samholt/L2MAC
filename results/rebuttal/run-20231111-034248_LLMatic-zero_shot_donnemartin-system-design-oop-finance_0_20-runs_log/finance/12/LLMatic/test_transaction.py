from transaction import Transaction

def test_add_transaction():
	transaction = Transaction()
	transaction.add_transaction('user1', 100, 'groceries', 'expense')
	assert len(transaction.transactions['user1']) == 1


def test_categorize_transaction():
	transaction = Transaction()
	transaction.add_transaction('user1', 100, 'groceries', 'expense')
	transaction_id = id(transaction.transactions['user1'][0])
	transaction.categorize_transaction('user1', transaction_id, 'entertainment')
	assert transaction.transactions['user1'][0]['category'] == 'entertainment'


def test_classify_recurring():
	transaction = Transaction()
	for _ in range(3):
		transaction.add_transaction('user1', 100, 'groceries', 'expense')
	transaction.classify_recurring('user1')
	assert transaction.transactions['user1'][0]['recurring'] == True
