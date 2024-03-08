from models.investment import Investment


class InvestmentController:
	@staticmethod
	def create_investment(account_name, balance, asset_allocation):
		return Investment(account_name, balance, asset_allocation)

	@staticmethod
	def link_account(investment, account_name):
		investment.link_account(account_name)

	@staticmethod
	def track_performance(investment):
		return investment.track_performance()

	@staticmethod
	def view_asset_allocation(investment):
		return investment.view_asset_allocation()

	@staticmethod
	def get_investments(user):
		# Mocking the database call with an in-memory list
		# In a real application, this would be a database call
		return [Investment('Savings', 1000, {'stocks': 50, 'bonds': 50})]
