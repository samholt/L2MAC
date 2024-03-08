from cryptography.fernet import Fernet
import hashlib
from datetime import datetime


class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = self.hash_password(password)
		self.key = Fernet.generate_key()
		self.cipher_suite = Fernet(self.key)
		self.email = self.encrypt_data(email)
		self.accounts = []
		self.budgets = {}
		self.log = []

	@staticmethod
	def hash_password(password):
		return hashlib.sha256(password.encode()).hexdigest()

	def encrypt_data(self, data):
		return self.cipher_suite.encrypt(data.encode()).decode()

	def decrypt_data(self, encrypted_data):
		return self.cipher_suite.decrypt(encrypted_data.encode()).decode()

	def authenticate(self, password):
		authenticated = self.password == self.hash_password(password)
		self.log.append(f'Authentication attempt with password: {"Success" if authenticated else "Failure"}')
		return authenticated

	def recover_password(self):
		self.log.append('Password recovery attempt')
		return self.password

	def set_budget(self, category, amount):
		self.budgets[category] = amount
		self.log.append(f'Set budget for {category}: {amount}')

	def check_budget(self, category):
		total_spent = sum([abs(transaction.amount) for account in self.accounts for transaction in account.transactions if transaction.category == category])
		self.log.append(f'Checked budget for {category}')
		return total_spent > self.budgets.get(category, 0)

	def track_progress(self, category):
		total_spent = sum([abs(transaction.amount) for account in self.accounts for transaction in account.transactions if transaction.category == category])
		self.log.append(f'Tracked progress for {category}')
		return total_spent / self.budgets.get(category, 0) if self.budgets.get(category) else 0

	def generate_monthly_report(self, month, year):
		income = 0
		expenses = 0
		for account in self.accounts:
			for transaction in account.transactions:
				if transaction.date.month == month and transaction.date.year == year:
					if transaction.amount > 0:
						income += transaction.amount
					else:
						expenses += transaction.amount
		self.log.append(f'Generated monthly report for {month}/{year}')
		return {'income': income, 'expenses': expenses, 'savings': income - expenses}

	def visualize_spending_habits(self):
		spending = {}
		for account in self.accounts:
			for transaction in account.transactions:
				if transaction.amount < 0:
					spending[transaction.category] = spending.get(transaction.category, 0) + abs(transaction.amount)
		self.log.append('Visualized spending habits')
		return spending

	def compare_year_on_year(self, year1, year2):
		report1 = {month: self.generate_monthly_report(month, year1) for month in range(1, 13)}
		report2 = {month: self.generate_monthly_report(month, year2) for month in range(1, 13)}
		comparison = {
			'income': sum([report1[month]['income'] for month in report1]) - sum([report2[month]['income'] for month in report2]),
			'expenses': sum([report1[month]['expenses'] for month in report1]) - sum([report2[month]['expenses'] for month in report2]),
			'savings': sum([report1[month]['savings'] for month in report1]) - sum([report2[month]['savings'] for month in report2])
		}
		self.log.append(f'Compared year on year for {year1} and {year2}')
		return comparison

	def get_savings_tips(self):
		spending = self.visualize_spending_habits()
		tips = []
		for category, amount in spending.items():
			if amount > self.budgets.get(category, 0):
				tips.append(f'You are overspending on {category}. Try to cut back.')
		self.log.append('Generated savings tips')
		return tips

	def get_product_recommendations(self):
		spending = self.visualize_spending_habits()
		recommendations = []
		for category, amount in spending.items():
			if amount > self.budgets.get(category, 0):
				recommendations.append(f'Consider a savings account for {category} expenses.')
		self.log.append('Generated product recommendations')
		return recommendations

	def get_notifications(self):
		notifications = []
		for account in self.accounts:
			for transaction in account.transactions:
				if transaction.date > datetime.now():
					notifications.append(f'Upcoming bill: {transaction.description} for {transaction.amount} on {transaction.date}')
				if transaction.amount < 0 and abs(transaction.amount) > account.balance * 0.5:
					notifications.append(f'Alert: Unusual activity detected. Large transaction of {transaction.amount}')
		self.log.append('Generated notifications')
		return notifications

