from models import User, Transaction, BankAccount, Budget, Investment

from collections import defaultdict
from datetime import datetime
import hashlib


class UserService:
	def __init__(self):
		self.users = {}

	def create_user(self, username, password, email):
		if username in self.users:
			return False
		user = User(username, hashlib.md5(password.encode()).hexdigest(), email)
		user.income = 1000
		user.spending = 1200
		user.savings = 200
		user.debt = 400
		self.users[username] = user
		return True

	def authenticate_user(self, username, password):
		if username in self.users and self.users[username].password == hashlib.md5(password.encode()).hexdigest():
			return True
		return False

	def recover_password(self, username):
		if username in self.users:
			return 'Cannot recover password for security reasons.'
		return None

	def provide_savings_tips(self, username):
		if username in self.users:
			user = self.users[username]
			tips = []
			if user.spending > user.income:
				tips.append('You are spending more than your income. Try to cut down on unnecessary expenses.')
			if user.savings < 0.2 * user.income:
				tips.append('You should aim to save at least 20% of your income.')
			return tips
		return None

	def recommend_financial_products(self, username):
		if username in self.users:
			user = self.users[username]
			recommendations = []
			if user.savings > 0.2 * user.income:
				recommendations.append('You have a good amount of savings. Consider investing in stocks or mutual funds.')
			if user.debt > 0.3 * user.income:
				recommendations.append('You have a high level of debt. Consider a debt consolidation loan.')
			return recommendations
		return None

	def send_notifications(self, username, message):
		if username in self.users:
			user = self.users[username]
			user.notifications.append(message)
			return True
		return False

	def alert_user(self, username, message):
		if username in self.users:
			user = self.users[username]
			user.alerts.append(message)
			return True
		return False

	def conduct_security_audit(self):
		for username, user in self.users.items():
			if user.password == hashlib.md5('123456'.encode()).hexdigest():
				self.alert_user(username, 'Your password is too weak. Please change it immediately.')

	def ensure_compliance(self):
		for username, user in self.users.items():
			if user.income > 10000:
				self.alert_user(username, 'Your income level requires additional verification. Please contact us immediately.')
