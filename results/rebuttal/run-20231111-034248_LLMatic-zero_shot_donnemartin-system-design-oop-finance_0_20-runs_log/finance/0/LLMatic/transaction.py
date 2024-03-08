import datetime

# Mock database
transactions_db = {}


def add_transaction(username, amount, category):
	if username not in transactions_db:
		transactions_db[username] = []
	transaction = {
		'date': datetime.datetime.now(),
		'amount': amount,
		'category': category,
		'recurring': False
	}
	transactions_db[username].append(transaction)
	return 'Transaction added successfully'


def categorize_transaction(username, transaction_index, category):
	if username in transactions_db and transaction_index < len(transactions_db[username]):
		transactions_db[username][transaction_index]['category'] = category
		return 'Transaction categorized successfully'
	else:
		return 'Invalid username or transaction index'


def identify_recurring_transactions(username):
	if username in transactions_db:
		transactions = transactions_db[username]
		for i in range(1, len(transactions)):
			if transactions[i]['amount'] == transactions[i-1]['amount'] and transactions[i]['category'] == transactions[i-1]['category']:
				transactions[i]['recurring'] = True
				transactions[i-1]['recurring'] = True
		return 'Recurring transactions identified'
	else:
		return 'Invalid username'
