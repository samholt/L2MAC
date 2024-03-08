from models.budget import Budget


class BudgetController:
	@staticmethod
	def create_budget(user, amount, category, month):
		return Budget(user, amount, category, month)

	@staticmethod
	def set_budget(budget, amount):
		budget.set_budget(amount)

	@staticmethod
	def adjust_budget(budget, amount):
		budget.adjust_budget(amount)

	@staticmethod
	def is_limit_nearing(budget, limit_percentage):
		return budget.is_limit_nearing(limit_percentage)

	@staticmethod
	def get_budgets(user):
		# Mocking the database call with an in-memory list
		# In a real application, this would be a database call
		return [Budget(user, 1000, 'groceries', 'January')]
