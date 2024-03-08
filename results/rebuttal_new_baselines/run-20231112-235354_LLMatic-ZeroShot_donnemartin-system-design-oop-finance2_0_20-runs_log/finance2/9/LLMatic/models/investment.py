class Investment:
	def __init__(self, user, type, amount, performance):
		self.user = user
		self.type = type
		self.amount = amount
		self.performance = performance

	def link_investment_account(self, account):
		self.account = account

	def track_investment_performance(self, performance):
		self.performance = performance

	def get_asset_allocation(self):
		return {'type': self.type, 'amount': self.amount}
