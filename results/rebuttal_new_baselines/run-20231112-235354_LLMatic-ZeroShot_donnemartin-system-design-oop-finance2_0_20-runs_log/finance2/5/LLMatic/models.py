class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email


class BankAccount:
	def __init__(self, account_number, bank_name, user_id):
		self.account_number = account_number
		self.bank_name = bank_name
		self.user_id = user_id
