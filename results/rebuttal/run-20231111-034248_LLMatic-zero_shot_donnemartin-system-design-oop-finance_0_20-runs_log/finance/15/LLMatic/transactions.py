class Transaction:
	def __init__(self):
		self.transactions = {}

	def add_income(self, user_id, amount, category):
		if user_id not in self.transactions:
			self.transactions[user_id] = []
		self.transactions[user_id].append({'id': len(self.transactions[user_id]), 'type': 'income', 'amount': amount, 'category': category})

	def add_expense(self, user_id, amount, category):
		if user_id not in self.transactions:
			self.transactions[user_id] = []
		self.transactions[user_id].append({'id': len(self.transactions[user_id]), 'type': 'expense', 'amount': amount, 'category': category})

	def get_transactions(self, user_id):
		if user_id in self.transactions:
			return self.transactions[user_id]
		return []

	def categorize_transaction(self, user_id, transaction_id, category):
		if user_id in self.transactions:
			for transaction in self.transactions[user_id]:
				if transaction['id'] == transaction_id:
					transaction['category'] = category
					return True
		return False
