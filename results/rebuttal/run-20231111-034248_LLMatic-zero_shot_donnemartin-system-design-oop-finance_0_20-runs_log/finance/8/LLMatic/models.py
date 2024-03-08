class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.linked_accounts = {}
		self.budget_goals = {}
		self.investments = {}
		self.notifications = []
		self.alerts = []

	@classmethod
	def create_user(cls, username, password, email):
		return cls(username, password, email)

	@staticmethod
	def user_exists(username):
		# This is a mock database
		users_db = {'test_user': {'password': 'test_password', 'email': 'test_email'}}
		return username in users_db

	@staticmethod
	def validate_password(username, password):
		# This is a mock database
		users_db = {'test_user': {'password': 'test_password', 'email': 'test_email'}}
		return users_db[username]['password'] == password if username in users_db else False

	def add_linked_account(self, bank_name, account_number):
		self.linked_accounts[bank_name] = account_number

	def remove_linked_account(self, bank_name):
		if bank_name in self.linked_accounts:
			del self.linked_accounts[bank_name]

	def import_transactions(self, bank_name):
		# Mock transactions data
		transactions_data = {
			'Bank1': [
				{'id': '1', 'type': 'income', 'amount': 1000, 'category': 'salary'},
				{'id': '2', 'type': 'expense', 'amount': 200, 'category': 'groceries'}
			],
			'Bank2': [
				{'id': '3', 'type': 'income', 'amount': 2000, 'category': 'salary'},
				{'id': '4', 'type': 'expense', 'amount': 300, 'category': 'rent'}
			]
		}
		return transactions_data[bank_name] if bank_name in transactions_data else []

	def set_budget_goal(self, category, amount):
		self.budget_goals[category] = amount

	def update_budget_goal(self, category, amount):
		if category in self.budget_goals:
			self.budget_goals[category] = amount

	def check_budget_progress(self, category):
		# Mock transactions data
		transactions_data = {
			'Bank1': [
				{'id': '1', 'type': 'income', 'amount': 1000, 'category': 'salary'},
				{'id': '2', 'type': 'expense', 'amount': 200, 'category': 'groceries'}
			],
			'Bank2': [
				{'id': '3', 'type': 'income', 'amount': 2000, 'category': 'salary'},
				{'id': '4', 'type': 'expense', 'amount': 300, 'category': 'rent'}
			]
		}
		# Calculate total expenses for the category
		total_expenses = sum(transaction['amount'] for bank in transactions_data for transaction in transactions_data[bank] if transaction['category'] == category)
		# Calculate progress towards the budget goal
		progress = total_expenses / self.budget_goals[category] if category in self.budget_goals else 0
		return progress

	def add_investment(self, investment_name, amount):
		self.investments[investment_name] = amount

	def update_investment(self, investment_name, amount):
		if investment_name in self.investments:
			self.investments[investment_name] = amount

	def delete_investment(self, investment_name):
		if investment_name in self.investments:
			del self.investments[investment_name]

	def calculate_roi(self, investment_name):
		# Mock investment returns data
		investment_returns = {
			'Investment1': 1.1,
			'Investment2': 1.2
		}
		return self.investments[investment_name] * investment_returns[investment_name] if investment_name in self.investments and investment_name in investment_returns else 0

	def generate_monthly_report(self):
		# Mock transactions data
		transactions_data = {
			'Bank1': [
				{'id': '1', 'type': 'income', 'amount': 1000, 'category': 'salary'},
				{'id': '2', 'type': 'expense', 'amount': 200, 'category': 'groceries'}
			],
			'Bank2': [
				{'id': '3', 'type': 'income', 'amount': 2000, 'category': 'salary'},
				{'id': '4', 'type': 'expense', 'amount': 300, 'category': 'rent'}
			]
		}
		# Calculate total income and expenses for each month
		monthly_report = {'income': 0, 'expense': 0}
		for bank in transactions_data:
			for transaction in transactions_data[bank]:
				monthly_report[transaction['type']] += transaction['amount']
		return monthly_report

	def generate_savings_tips(self):
		# Mock transactions data
		transactions_data = {
			'Bank1': [
				{'id': '1', 'type': 'income', 'amount': 1000, 'category': 'salary'},
				{'id': '2', 'type': 'expense', 'amount': 200, 'category': 'groceries'}
			],
			'Bank2': [
				{'id': '3', 'type': 'income', 'amount': 2000, 'category': 'salary'},
				{'id': '4', 'type': 'expense', 'amount': 300, 'category': 'rent'}
			]
		}
		# Calculate total income and expenses for each month
		monthly_report = {'income': 0, 'expense': 0}
		for bank in transactions_data:
			for transaction in transactions_data[bank]:
				monthly_report[transaction['type']] += transaction['amount']
		# Calculate savings
		savings = monthly_report['income'] - monthly_report['expense']
		# Generate savings tips based on savings
		if savings < 500:
			return 'Consider cutting down on non-essential expenses.'
		elif savings < 1000:
			return 'Good job! You might want to consider investing some of your savings.'
		else:
			return 'Excellent! You have a high savings rate. Consider increasing your investments.'

	def recommend_financial_products(self):
		# Mock financial products data
		financial_products = {
			'Investment1': {'min_investment': 1000, 'return_rate': 1.1},
			'Investment2': {'min_investment': 2000, 'return_rate': 1.2}
		}
		# Recommend financial products based on user's investments
		recommendations = [product for product, details in financial_products.items() if details['min_investment'] <= sum(self.investments.values())]
		return recommendations

	def add_notification(self, notification):
		self.notifications.append(notification)

	def remove_notification(self, notification):
		if notification in self.notifications:
			self.notifications.remove(notification)

	def add_alert(self, alert):
		self.alerts.append(alert)

	def remove_alert(self, alert):
		if alert in self.alerts:
			self.alerts.remove(alert)

	def check_for_unusual_activity(self):
		# Mock transactions data
		transactions_data = {
			'Bank1': [
				{'id': '1', 'type': 'income', 'amount': 1000, 'category': 'salary'},
				{'id': '2', 'type': 'expense', 'amount': 200, 'category': 'groceries'}
			],
			'Bank2': [
				{'id': '3', 'type': 'income', 'amount': 2000, 'category': 'salary'},
				{'id': '4', 'type': 'expense', 'amount': 300, 'category': 'rent'}
			]
		}
		# Check for transactions with amount greater than 1000
		unusual_transactions = [transaction for bank in transactions_data for transaction in transactions_data[bank] if transaction['amount'] > 1000]
		if unusual_transactions:
			self.add_alert('Unusual activity detected in your account.')
		return unusual_transactions
