from models.investment import Investment


class InvestmentView:
	@staticmethod
	def create_investment(user, amount, type):
		return Investment.create_investment(user, amount, type)

	@staticmethod
	def get_user_investments(user):
		return Investment.get_user_investments(user)

	@staticmethod
	def track_investment_performance(user):
		return Investment.track_investment_performance(user)
