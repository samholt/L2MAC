class Investment:
	def __init__(self):
		self.accounts = {}
		self.performance = {}
		self.balance = 0

	def integrate_account(self, account_name, account):
		self.accounts[account_name] = account
		self.update_balance()
		self.update_performance()

	def update_balance(self):
		self.balance = sum(account.balance for account in self.accounts.values())

	def update_performance(self):
		for account_name, account in self.accounts.items():
			self.performance[account_name] = account.get_performance()

	def get_asset_allocation(self):
		allocation = {}
		for account_name, account in self.accounts.items():
			for asset, amount in account.get_assets().items():
				if asset not in allocation:
					allocation[asset] = 0
				allocation[asset] += amount
		return allocation
