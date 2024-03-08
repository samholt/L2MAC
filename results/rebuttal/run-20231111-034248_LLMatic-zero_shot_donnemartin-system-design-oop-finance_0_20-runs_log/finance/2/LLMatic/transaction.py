import datetime

# Mock database
transactions_db = {}


class Transaction:
	def __init__(self, username, amount, category, recurring):
		self.username = username
		self.amount = amount
		self.category = category
		self.recurring = recurring
		self.date = datetime.datetime.now()


def add_transaction(username, amount, category, recurring=False):
	if username not in transactions_db:
		transactions_db[username] = []
	transaction = Transaction(username, amount, category, recurring)
	transactions_db[username].append(transaction)
	return True


def get_transactions(username):
	if username not in transactions_db:
		return None
	return transactions_db[username]


def get_recurring_transactions(username):
	if username not in transactions_db:
		return None
	return [transaction for transaction in transactions_db[username] if transaction.recurring]
