class Transaction:
	def __init__(self, id, amount, date, type):
		self.id = id
		self.amount = float(amount)
		self.date = date
		self.type = type


class TransactionManager:
	def __init__(self):
		self.transactions = {}

	def add_transaction(self, id, amount, date, type):
		if id not in self.transactions:
			self.transactions[id] = Transaction(id, amount, date, type)

	def get_transaction(self, id):
		return self.transactions.get(id, None)

	def delete_transaction(self, id):
		if id in self.transactions:
			del self.transactions[id]
