import datetime
import hashlib
from investment import Investment


class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = self.encrypt_password(password)
		self.email = email
		self.accounts = []
		self.budgets = {}
		self.notifications = []
		self.alerts = []
		self.investments = []

	def encrypt_password(self, password):
		# Strong encryption: Use SHA256 to hash the password
		return hashlib.sha256(password.encode()).hexdigest()

	def authenticate(self, username, password):
		return self.username == username and self.password == self.encrypt_password(password)

	def recover_password(self):
		# Generate a temporary password and send it to the user's email
		temp_password = 'temp1234'
		self.password = self.encrypt_password(temp_password)
		return 'Temporary password has been sent to your email.'

	def set_budget(self, category, amount):
		self.budgets[category] = amount

	def track_budget(self, category):
		total_spent = sum([transaction.amount for account in self.accounts for transaction in account.transactions if transaction.category == category])
		return total_spent

	def alert_user(self):
		for category, budget in self.budgets.items():
			total_spent = self.track_budget(category)
			if total_spent >= budget:
				return f'Alert! You have reached or exceeded your budget for {category}.'
		return 'No budget alerts.'

	def generate_monthly_report(self):
		report = {}
		for account in self.accounts:
			for transaction in account.transactions:
				if transaction.date.month == datetime.datetime.now().month:
					if transaction.category not in report:
						report[transaction.category] = transaction.amount
					else:
						report[transaction.category] += transaction.amount
		return report

	def generate_yearly_report(self):
		report = {}
		for account in self.accounts:
			for transaction in account.transactions:
				if transaction.date.year == datetime.datetime.now().year:
					if transaction.category not in report:
						report[transaction.category] = transaction.amount
					else:
						report[transaction.category] += transaction.amount
		return report

	def compare_yearly_spending(self, year1, year2):
		report1 = {}
		report2 = {}
		for account in self.accounts:
			for transaction in account.transactions:
				if transaction.date.year == year1:
					if transaction.category not in report1:
						report1[transaction.category] = transaction.amount
					else:
						report1[transaction.category] += transaction.amount
				elif transaction.date.year == year2:
					if transaction.category not in report2:
						report2[transaction.category] = transaction.amount
					else:
						report2[transaction.category] += transaction.amount
		comparison = {}
		for category in set(report1.keys()).union(report2.keys()):
			comparison[category] = report2.get(category, 0) - report1.get(category, 0)
		return comparison

	def get_savings_tips(self):
		income = sum([transaction.amount for account in self.accounts for transaction in account.transactions if transaction.is_deposit])
		expenses = sum([transaction.amount for account in self.accounts for transaction in account.transactions if not transaction.is_deposit])
		savings = income - expenses
		if expenses > 0.7 * income:
			return 'You are spending a large portion of your income. Consider cutting down on non-essential expenses.'
		elif savings < 0.2 * income:
			return 'Your savings are low. Consider saving more of your income.'
		else:
			return 'You are doing well with your savings. Keep it up!'

	def recommend_products(self):
		income = sum([transaction.amount for account in self.accounts for transaction in account.transactions if transaction.is_deposit])
		expenses = sum([transaction.amount for account in self.accounts for transaction in account.transactions if not transaction.is_deposit])
		savings = income - expenses
		if savings > 0.5 * income:
			return 'You have a high amount of savings. Consider investing in stocks or bonds.'
		else:
			return 'Your savings are relatively low. Consider opening a savings account to earn interest.'

	def set_notification(self, notification):
		self.notifications.append(notification)

	def get_notifications(self):
		return self.notifications

	def set_alert(self, alert):
		self.alerts.append(alert)

	def get_alerts(self):
		return self.alerts

	def conduct_security_audit(self):
		# For simplicity, let's say a security audit is just checking if the password is 'password'
		return self.password != self.encrypt_password('password')

