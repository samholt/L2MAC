class BankAccount:
	def __init__(self):
		self.bank_accounts = {}

	def link_bank_account(self, user_id, bank_account_details):
		if user_id not in self.bank_accounts:
			self.bank_accounts[user_id] = []
		self.bank_accounts[user_id].append(bank_account_details)

	def import_transactions(self, user_id, transactions):
		if user_id in self.bank_accounts:
			for account in self.bank_accounts[user_id]:
				account['transactions'].extend(transactions)

	def update_account_balance(self, user_id):
		if user_id in self.bank_accounts:
			for account in self.bank_accounts[user_id]:
				account['balance'] = sum(transaction['amount'] for transaction in account['transactions'])
