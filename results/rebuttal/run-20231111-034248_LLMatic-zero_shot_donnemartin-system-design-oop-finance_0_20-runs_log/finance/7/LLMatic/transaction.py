class Transaction:
	def __init__(self):
		self.transactions = {}

	def add_income(self, user_id, amount, category):
		if user_id not in self.transactions:
			self.transactions[user_id] = []
		self.transactions[user_id].append({'type': 'income', 'amount': amount, 'category': category})

	def add_expense(self, user_id, amount, category):
		if user_id not in self.transactions:
			self.transactions[user_id] = []
		self.transactions[user_id].append({'type': 'expense', 'amount': amount, 'category': category})

	def categorize_transaction(self, user_id, transaction_index, category):
		if user_id in self.transactions and len(self.transactions[user_id]) > transaction_index:
			self.transactions[user_id][transaction_index]['category'] = category

	def identify_recurring_transactions(self, user_id):
		if user_id not in self.transactions:
			return []
		recurring_transactions = []
		for i in range(len(self.transactions[user_id]) - 1):
			if self.transactions[user_id][i] == self.transactions[user_id][i + 1]:
				recurring_transactions.append(self.transactions[user_id][i])
		return recurring_transactions
