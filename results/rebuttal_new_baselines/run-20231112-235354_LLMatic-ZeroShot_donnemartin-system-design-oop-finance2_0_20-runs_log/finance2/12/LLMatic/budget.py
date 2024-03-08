class Budget:
	def __init__(self):
		self.budget_data = {}

	def set_budget(self, user_id, amount):
		self.budget_data[user_id] = amount

	def adjust_budget(self, user_id, amount):
		if user_id in self.budget_data:
			self.budget_data[user_id] += amount
		else:
			self.budget_data[user_id] = amount

	def get_budget(self, user_id):
		return self.budget_data.get(user_id, 0)
