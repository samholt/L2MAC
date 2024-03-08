class Account:
	def __init__(self):
		self.users = {}
		self.linked_bank_accounts = {}

	def create_account(self, user_id, user_info):
		self.users[user_id] = user_info

	def link_bank_account(self, user_id, bank_account_info):
		if user_id not in self.users:
			raise Exception('User does not exist')
		self.linked_bank_accounts[user_id] = bank_account_info

	def handle_mfa(self, user_id, mfa_info):
		if user_id not in self.users:
			raise Exception('User does not exist')
		self.users[user_id]['mfa_info'] = mfa_info
