from datetime import datetime

# Mock database
investments_db = {}

class Investment:
	def __init__(self, user, amount, type):
		self.user = user
		self.amount = amount
		self.type = type
		self.date = datetime.now()

	@classmethod
	def create_investment(cls, user, amount, type):
		investment = cls(user, amount, type)
		investments_db[user] = investments_db.get(user, []) + [investment]
		return investment

	@classmethod
	def get_user_investments(cls, user):
		return investments_db.get(user, [])

	@classmethod
	def track_investment_performance(cls, user):
		# Mock performance tracking
		return {investment.type: investment.amount * 1.05 for investment in cls.get_user_investments(user)}
