class Investment:
	def __init__(self, account_name, balance, asset_allocation):
		self.account_name = account_name
		self.balance = balance
		self.asset_allocation = asset_allocation

	def link_account(self, account_name):
		self.account_name = account_name

	def track_performance(self):
		return self.balance

	def view_asset_allocation(self):
		return self.asset_allocation

	def to_dict(self):
		return {
			'account_name': self.account_name,
			'balance': self.balance,
			'asset_allocation': self.asset_allocation
		}
