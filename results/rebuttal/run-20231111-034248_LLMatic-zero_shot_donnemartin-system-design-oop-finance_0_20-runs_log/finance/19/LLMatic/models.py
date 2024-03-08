class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.bank_account = BankAccount('12345678', 'Test Bank', 0)

class Category:
	def __init__(self, name):
		self.name = name

class Transaction:
	def __init__(self, category, amount, date):
		self.category = category
		self.amount = amount
		self.date = date

class BankAccount:
	def __init__(self, account_number, bank_name, balance):
		self.account_number = account_number
		self.bank_name = bank_name
		self.balance = balance
		self.transactions = []

	def add_transaction(self, transaction):
		self.transactions.append(transaction)
		self.balance -= transaction.amount

class Budget:
	def __init__(self, category, amount, month):
		self.category = category
		self.amount = amount
		self.month = month

class Investment:
	def __init__(self, name, amount_invested, current_value):
		self.name = name
		self.amount_invested = amount_invested
		self.current_value = current_value
