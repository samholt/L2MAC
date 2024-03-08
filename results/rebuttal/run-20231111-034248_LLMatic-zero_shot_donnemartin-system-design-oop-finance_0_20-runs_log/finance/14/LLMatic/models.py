class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email

class Category:
	def __init__(self, name):
		self.name = name

class Transaction:
	def __init__(self, amount, date, category):
		self.amount = amount
		self.date = date
		self.category = category

	def is_equal(self, transaction):
		return self.amount == transaction.amount and self.date == transaction.date and self.category == transaction.category

class BankAccount:
	def __init__(self, account_number, bank_name, balance):
		self.account_number = account_number
		self.bank_name = bank_name
		self.balance = balance

class Budget:
	def __init__(self, category, limit, user):
		self.category = category
		self.limit = limit
		self.user = user

class Investment:
	def __init__(self, name, current_value, roi):
		self.name = name
		self.current_value = current_value
		self.roi = roi
