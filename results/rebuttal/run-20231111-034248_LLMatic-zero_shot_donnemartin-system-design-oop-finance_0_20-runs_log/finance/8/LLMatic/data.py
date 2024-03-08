class Transaction:
	def __init__(self, id, type, amount, category):
		self.id = id
		self.type = type
		self.amount = amount
		self.category = category


class Data:
	def __init__(self):
		self.transactions = {}

	def add_transaction(self, transaction):
		self.transactions[transaction.id] = transaction

	def update_transaction(self, id, type, amount, category):
		if id in self.transactions:
			self.transactions[id].type = type
			self.transactions[id].amount = amount
			self.transactions[id].category = category

	def delete_transaction(self, id):
		if id in self.transactions:
			del self.transactions[id]

	def categorize_transactions(self):
		categories = {}
		for transaction in self.transactions.values():
			if transaction.category not in categories:
				categories[transaction.category] = []
			categories[transaction.category].append(transaction)
		return categories

	def generate_spending_trends(self):
		# Categorize transactions by type
		categories = self.categorize_transactions()
		# Calculate total amount for each category
		spending_trends = {category: sum(transaction.amount for transaction in transactions) for category, transactions in categories.items()}
		return spending_trends
