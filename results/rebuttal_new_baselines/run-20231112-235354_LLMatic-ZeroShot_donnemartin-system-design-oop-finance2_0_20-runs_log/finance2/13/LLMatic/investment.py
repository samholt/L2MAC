class Investment:
	def __init__(self):
		self.accounts = {}
		self.performance = {}
		self.balance = 0

	def link_account(self, account_name, account):
		# Link an investment account
		self.accounts[account_name] = account
		self.balance += account['balance']

	def track_performance(self, account_name, performance):
		# Track the performance of an investment
		self.performance[account_name] = performance

	def get_balance(self):
		# Get the balance of the investments
		return self.balance

	def get_asset_allocation(self):
		# Get the asset allocation
		allocation = {}
		for account_name, account in self.accounts.items():
			for asset, amount in account['assets'].items():
				if asset not in allocation:
					allocation[asset] = 0
				allocation[asset] += amount
		return allocation
