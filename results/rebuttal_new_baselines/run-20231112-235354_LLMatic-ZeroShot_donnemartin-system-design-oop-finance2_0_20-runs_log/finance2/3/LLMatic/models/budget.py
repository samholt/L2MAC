class Budget:
	def __init__(self, user, amount, category):
		self.user = user
		self.amount = amount
		self.category = category

	@staticmethod
	def set_budget(user, amount, category):
		# Mocking setting budget
		return {'user': user, 'amount': amount, 'category': category}

	@staticmethod
	def adjust_budget(user, amount):
		# Mocking adjusting budget
		return {'user': user, 'amount': amount}

	@staticmethod
	def get_user_budgets(user):
		# Mocking getting user budgets
		return [{'user': user, 'amount': 500, 'category': 'Groceries'}]
