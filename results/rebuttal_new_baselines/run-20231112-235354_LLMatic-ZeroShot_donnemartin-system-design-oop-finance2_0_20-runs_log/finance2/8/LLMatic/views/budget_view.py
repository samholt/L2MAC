from models.budget import Budget


class BudgetView:
	@staticmethod
	def set_budget(user, amount, category):
		budget = Budget(user, amount, category)
		budget.set_budget(user, amount, category)
		return budget

	@staticmethod
	def adjust_budget(user, amount, category):
		budget = Budget(user, amount, category)
		budget.adjust_budget(user, amount)
		return budget

	@staticmethod
	def get_budgets(user, amount, category):
		budget = Budget(user, amount, category)
		return budget.get_budgets(user)
