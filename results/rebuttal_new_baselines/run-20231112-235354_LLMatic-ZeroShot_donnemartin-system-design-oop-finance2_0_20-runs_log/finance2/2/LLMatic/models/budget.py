class Budget:
	def __init__(self, user, amount, category, month):
		self.user = user
		self.amount = amount
		self.category = category
		self.month = month

	def to_dict(self):
		return {
			'user': self.user,
			'amount': self.amount,
			'category': self.category,
			'month': self.month
		}

	def set_budget(self, amount):
		self.amount = amount

	def adjust_budget(self, amount):
		self.amount += amount

	def is_limit_nearing(self, limit_percentage):
		return self.amount <= self.amount * limit_percentage / 100
