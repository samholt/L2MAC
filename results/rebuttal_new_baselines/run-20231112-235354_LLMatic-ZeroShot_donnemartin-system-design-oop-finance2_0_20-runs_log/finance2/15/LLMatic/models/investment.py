class Investment:
	def __init__(self, user, account_name, balance, asset_allocation):
		self.user = user
		self.account_name = account_name
		self.balance = balance
		self.asset_allocation = asset_allocation
		self.linked_accounts = []

	def link_account(self, account):
		self.linked_accounts.append(account)

	def get_accounts(self):
		return self.linked_accounts
