class Transaction:
	def __init__(self):
		self.transactions = {}

	def add_transaction(self, user_id, amount, category, date):
		if user_id not in self.transactions:
			self.transactions[user_id] = []
		self.transactions[user_id].append({'amount': amount, 'category': category, 'date': date})

	def categorize_transaction(self, user_id, transaction_id, category):
		for transaction in self.transactions[user_id]:
			if id(transaction) == transaction_id:
				transaction['category'] = category

	def classify_recurring_transactions(self, user_id):
		recurring_transactions = []
		transaction_counts = {}
		for transaction in self.transactions[user_id]:
			transaction_tuple = (transaction['amount'], transaction['category'])
			if transaction_tuple not in transaction_counts:
				transaction_counts[transaction_tuple] = 0
			transaction_counts[transaction_tuple] += 1
		for transaction, count in transaction_counts.items():
			if count > 1:
				recurring_transactions.append(transaction)
		return recurring_transactions
