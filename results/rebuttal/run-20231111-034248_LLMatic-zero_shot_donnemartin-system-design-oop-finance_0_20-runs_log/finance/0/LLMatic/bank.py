import random

# Mock database
linked_accounts_db = {}
transactions_db = {}


def link_account(username, bank_account_number):
	if username not in linked_accounts_db:
		linked_accounts_db[username] = []
	linked_accounts_db[username].append(bank_account_number)
	return 'Bank account linked successfully'


def import_transactions(username, bank_account_number):
	if username in linked_accounts_db and bank_account_number in linked_accounts_db[username]:
		if username not in transactions_db:
			transactions_db[username] = []
		for _ in range(10):
			transaction = {
				'bank_account_number': bank_account_number,
				'amount': random.randint(-1000, 1000),
				'date': '2022-01-01'
			}
			transactions_db[username].append(transaction)
		return 'Transactions imported successfully'
	else:
		return 'Invalid username or bank account number'


def update_account_balance(username, bank_account_number):
	if username in linked_accounts_db and bank_account_number in linked_accounts_db[username]:
		balance = 0
		for transaction in transactions_db[username]:
			if transaction['bank_account_number'] == bank_account_number:
				balance += transaction['amount']
		return balance
	else:
		return 'Invalid username or bank account number'
