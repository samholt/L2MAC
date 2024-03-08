class Account:
	def __init__(self, account_name, balance):
		self.account_name = account_name
		self.balance = balance
		self.assets = {}

	def get_balance(self):
		return self.balance

	def buy_asset(self, asset_name, amount):
		if asset_name not in self.assets:
			self.assets[asset_name] = 0
		self.assets[asset_name] += amount
		self.balance -= amount

	def sell_asset(self, asset_name, amount):
		if asset_name in self.assets and self.assets[asset_name] >= amount:
			self.assets[asset_name] -= amount
			self.balance += amount

	def get_assets(self):
		return self.assets

	def get_performance(self):
		return sum(self.assets.values())
