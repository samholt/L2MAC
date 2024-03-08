class User:
	def __init__(self, username, password, email, income=0, spending=0, savings=0, debt=0):
		self.username = username
		self.password = password
		self.email = email
		self.income = income
		self.spending = spending
		self.savings = savings
		self.debt = debt
		self.notifications = []
		self.alerts = []

class Transaction:
	def __init__(self, amount, category, date):
		self.amount = amount
		self.category = category
		self.date = date

class BankAccount:
	def __init__(self, account_number, bank_name, balance):
		self.account_number = account_number
		self.bank_name = bank_name
		self.balance = balance

class Budget:
	def __init__(self, category, limit):
		self.category = category
		self.limit = limit
		self.progress = 0

class Investment:
	def __init__(self, investment_type, amount_invested, current_value):
		self.investment_type = investment_type
		self.amount_invested = amount_invested
		self.current_value = current_value
