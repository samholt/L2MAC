class Bank:
	def __init__(self):
		self.accounts = {}

	def link_account(self, user_id, account_number, bank_name):
		if user_id not in self.accounts:
			self.accounts[user_id] = []
		self.accounts[user_id].append({'account_number': account_number, 'bank_name': bank_name, 'balance': 0})

	def import_transactions(self, user_id, account_number, transactions):
		for account in self.accounts[user_id]:
			if account['account_number'] == account_number:
				for transaction in transactions:
					account['balance'] += transaction['amount']

	def update_balance(self, user_id, account_number, new_balance):
		for account in self.accounts[user_id]:
			if account['account_number'] == account_number:
				account['balance'] = new_balance
