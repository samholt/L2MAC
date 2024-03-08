class Transaction:
	def __init__(self):
		self.transactions = {}

	def add_transaction(self, user_id, amount, category, transaction_type, recurring=False):
		if user_id not in self.transactions:
			self.transactions[user_id] = []
		self.transactions[user_id].append({
			'id': len(self.transactions[user_id]),
			'amount': amount,
			'category': category,
			'transaction_type': transaction_type,
			'recurring': recurring
		})

	def categorize_transaction(self, user_id, transaction_id, category):
		if user_id in self.transactions:
			for transaction in self.transactions[user_id]:
				if transaction['id'] == transaction_id:
					transaction['category'] = category
					return 'Transaction categorized successfully'
		return 'Transaction not found'

	def classify_recurring_transactions(self, user_id):
		if user_id in self.transactions:
			recurring_transactions = []
			for transaction in self.transactions[user_id]:
				if transaction['recurring']:
					recurring_transactions.append(transaction)
			return recurring_transactions
		return 'No transactions found'
