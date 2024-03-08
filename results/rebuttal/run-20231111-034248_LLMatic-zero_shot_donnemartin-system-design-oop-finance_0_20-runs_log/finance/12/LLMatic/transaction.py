class Transaction:
	def __init__(self):
		self.transactions = {}

	def add_transaction(self, user_id, amount, category, transaction_type):
		if user_id not in self.transactions:
			self.transactions[user_id] = []
		self.transactions[user_id].append({
			'amount': amount,
			'category': category,
			'type': transaction_type,
			'recurring': False
		})

	def categorize_transaction(self, user_id, transaction_id, category):
		if user_id in self.transactions:
			for transaction in self.transactions[user_id]:
				if id(transaction) == transaction_id:
					transaction['category'] = category

	def classify_recurring(self, user_id):
		if user_id in self.transactions:
			transaction_count = {}
			for transaction in self.transactions[user_id]:
				key = (transaction['amount'], transaction['category'], transaction['type'])
				if key not in transaction_count:
					transaction_count[key] = 0
				transaction_count[key] += 1
				if transaction_count[key] > 2:
					for trans in self.transactions[user_id]:
						if (trans['amount'], trans['category'], trans['type']) == key:
							trans['recurring'] = True
