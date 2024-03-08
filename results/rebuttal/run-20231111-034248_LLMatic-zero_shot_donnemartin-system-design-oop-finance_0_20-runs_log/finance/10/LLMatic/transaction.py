class Transaction:
	def __init__(self):
		self.transactions = {}

	def add_transaction(self, user_id, transaction):
		if user_id not in self.transactions:
			self.transactions[user_id] = []
		self.transactions[user_id].append(transaction)

	def categorize_transactions(self, user_id):
		if user_id not in self.transactions:
			return {}
		categories = {}
		for transaction in self.transactions[user_id]:
			category = transaction['category']
			if category not in categories:
				categories[category] = []
			categories[category].append(transaction)
		return categories

	def identify_recurring_transactions(self, user_id):
		if user_id not in self.transactions:
			return []
		recurring = []
		for transaction in self.transactions[user_id]:
			if transaction['recurring']:
				recurring.append(transaction)
		return recurring
