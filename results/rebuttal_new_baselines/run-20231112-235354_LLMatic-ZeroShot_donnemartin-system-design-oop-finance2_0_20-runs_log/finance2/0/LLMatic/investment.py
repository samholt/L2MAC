class Investment:
	def __init__(self):
		self.investment_accounts = {}
		self.asset_allocation = {}

	def integrate_investment_account(self, user_id, account_info):
		self.investment_accounts[user_id] = account_info

	def track_investment(self, user_id, investment_info):
		self.investment_accounts[user_id].update(investment_info)

	def overview_asset_allocation(self, user_id, allocation_info):
		self.asset_allocation[user_id] = allocation_info
