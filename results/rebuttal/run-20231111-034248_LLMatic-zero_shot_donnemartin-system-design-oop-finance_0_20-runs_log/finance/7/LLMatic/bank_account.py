class BankAccount:
	def __init__(self):
		self.bank_accounts = {}

	def link_bank_account(self, user_id, bank_name, account_number):
		if user_id not in self.bank_accounts:
			self.bank_accounts[user_id] = []
		self.bank_accounts[user_id].append({
			'bank_name': bank_name,
			'account_number': account_number,
			'balance': 0
		})

	def import_transactions(self, user_id, account_number, transactions):
		for account in self.bank_accounts[user_id]:
			if account['account_number'] == account_number:
				for transaction in transactions:
					account['balance'] += transaction['amount']

	def update_balance(self, user_id, account_number, new_balance):
		for account in self.bank_accounts[user_id]:
			if account['account_number'] == account_number:
				account['balance'] = new_balance
