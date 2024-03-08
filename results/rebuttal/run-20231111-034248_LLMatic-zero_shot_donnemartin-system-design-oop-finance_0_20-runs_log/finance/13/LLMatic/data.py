import datetime

class Transaction:
	def __init__(self, id, type, amount, category, date):
		self.id = id
		self.type = type
		self.amount = amount
		self.category = category
		self.date = date

class BankAccount:
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.transactions = []

	def import_transactions(self, transactions):
		self.transactions.extend(transactions)

class Investment:
	def __init__(self, id, name, amount):
		self.id = id
		self.name = name
		self.amount = amount
		self.performance = 0

	def update_performance(self, performance):
		self.performance = performance

	def set_alert(self, alert_value):
		self.alert_value = alert_value

	def check_alert(self):
		if self.performance >= self.alert_value:
			return 'Alert: Investment ' + self.name + ' has reached the alert value.'
		else:
			return 'No alert'

class Data:
	def __init__(self):
		self.transactions = {}
		self.bank_accounts = {}
		self.budget_goals = {}
		self.investments = {}

	def add_transaction(self, transaction):
		self.transactions[transaction.id] = transaction

	def edit_transaction(self, id, type=None, amount=None, category=None):
		if id in self.transactions:
			if type is not None:
				self.transactions[id].type = type
			if amount is not None:
				self.transactions[id].amount = amount
			if category is not None:
				self.transactions[id].category = category

	def delete_transaction(self, id):
		if id in self.transactions:
			del self.transactions[id]

	def get_transaction(self, id):
		return self.transactions.get(id, None)

	def get_all_transactions(self):
		return list(self.transactions.values())

	def add_bank_account(self, bank_account):
		self.bank_accounts[bank_account.id] = bank_account

	def remove_bank_account(self, id):
		if id in self.bank_accounts:
			del self.bank_accounts[id]

	def get_bank_account(self, id):
		return self.bank_accounts.get(id, None)

	def import_transactions_from_bank_account(self, id, transactions):
		if id in self.bank_accounts:
			self.bank_accounts[id].import_transactions(transactions)
			for transaction in transactions:
				self.add_transaction(transaction)

	def set_budget_goal(self, category, amount):
		self.budget_goals[category] = amount

	def get_budget_goal(self, category):
		return self.budget_goals.get(category, None)

	def track_budget_progress(self, category):
		budget_goal = self.get_budget_goal(category)
		if budget_goal is None:
			return None
		total_expense = sum(transaction.amount for transaction in self.get_all_transactions() if transaction.category == category and transaction.type == 'expense')
		return total_expense / budget_goal if budget_goal != 0 else 0

	def alert_budget_limit(self, category):
		progress = self.track_budget_progress(category)
		if progress is None:
			return None
		if progress > 1:
			return 'You have exceeded your budget limit for ' + category
		elif progress >= 0.9:
			return 'You are nearing your budget limit for ' + category
		else:
			return 'You are within your budget limit for ' + category

	def add_investment(self, investment):
		self.investments[investment.id] = investment

	def remove_investment(self, id):
		if id in self.investments:
			del self.investments[id]

	def get_investment(self, id):
		return self.investments.get(id, None)

	def update_investment_performance(self, id, performance):
		if id in self.investments:
			self.investments[id].update_performance(performance)

	def set_investment_alert(self, id, alert_value):
		if id in self.investments:
			self.investments[id].set_alert(alert_value)

	def check_investment_alert(self, id):
		if id in self.investments:
			return self.investments[id].check_alert()

	def generate_monthly_report(self, month, year):
		monthly_transactions = [transaction for transaction in self.get_all_transactions() if transaction.date.month == month and transaction.date.year == year]
		report = {}
		for transaction in monthly_transactions:
			if transaction.category not in report:
				report[transaction.category] = 0
			report[transaction.category] += transaction.amount
		return report

	def generate_spending_trends(self):
		transactions = self.get_all_transactions()
		trends = {}
		for transaction in transactions:
			if transaction.category not in trends:
				trends[transaction.category] = [0] * 12
			trends[transaction.category][transaction.date.month - 1] += transaction.amount
		return trends

	def generate_yearly_comparison(self):
		transactions = self.get_all_transactions()
		comparison = {}
		for transaction in transactions:
			if transaction.date.year not in comparison:
				comparison[transaction.date.year] = 0
			comparison[transaction.date.year] += transaction.amount
		return comparison

	def generate_savings_tips(self):
		tips = []
		for category, budget in self.budget_goals.items():
			progress = self.track_budget_progress(category)
			if progress > 1:
				tips.append('Consider reducing your spending on ' + category + '.')
			elif progress < 0.5:
				tips.append('You are spending less than half of your budget on ' + category + '. Consider if you can reallocate this budget.')
		return tips

	def recommend_financial_products(self):
		products = ['High interest savings account', 'Low interest credit card', 'Investment in index funds']
		recommendations = []
		for product in products:
			recommendations.append('Consider ' + product + ' to improve your financial health.')
		return recommendations

	def send_notification(self, message):
		return 'Notification: ' + message

	def alert_unusual_activity(self, transaction):
		average = sum(t.amount for t in self.transactions.values() if t.category == transaction.category) / len(self.transactions)
		if transaction.amount > average * 2:
			return self.send_notification('Unusual activity detected in ' + transaction.category + ' transactions.')
		return 'No unusual activity detected.'

