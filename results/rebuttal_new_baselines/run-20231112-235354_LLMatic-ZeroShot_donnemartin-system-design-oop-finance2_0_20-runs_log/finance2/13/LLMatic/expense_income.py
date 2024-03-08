from datetime import datetime

class Expense:
	def __init__(self, amount, category):
		self.amount = amount
		self.category = category
		self.date = datetime.now()

	def add_expense(self, amount, category):
		# Add an expense
		self.amount = amount
		self.category = category
		self.date = datetime.now()

	def view_expense(self):
		# View the expense
		return {'amount': self.amount, 'category': self.category, 'date': self.date}

class Income:
	def __init__(self, amount, category):
		self.amount = amount
		self.category = category
		self.date = datetime.now()

	def add_income(self, amount, category):
		# Add an income
		self.amount = amount
		self.category = category
		self.date = datetime.now()

	def view_income(self):
		# View the income
		return {'amount': self.amount, 'category': self.category, 'date': self.date}
