from models import User, Transaction, Category, BankAccount, Budget, Investment

from datetime import datetime
import calendar


class UserService:
	def __init__(self):
		self.users = {}

	def create_user(self, username, password, email):
		if username in self.users:
			return 'User already exists'
		self.users[username] = User(username, self.encrypt_password(password), email)
		return 'User created successfully'

	def authenticate_user(self, username, password):
		if username in self.users and self.users[username].password == self.encrypt_password(password):
			return 'User authenticated'
		return 'Authentication failed'

	def recover_password(self, username):
		if username in self.users:
			return self.users[username].password
		return 'User not found'

	def get_savings_tips(self, username):
		if username not in self.users:
			return 'User not found'
		user = self.users[username]
		tips = []
		if user.bank_account.balance < 500:
			tips.append('Consider saving more money')
		if user.bank_account.balance > 1000:
			tips.append('Consider investing some money')
		return tips

	def get_product_recommendations(self, username):
		if username not in self.users:
			return 'User not found'
		user = self.users[username]
		recommendations = []
		if user.bank_account.balance < 500:
			recommendations.append('Consider a high-interest savings account')
		if user.bank_account.balance > 1000:
			recommendations.append('Consider a low-risk investment product')
		return recommendations

	def send_notifications(self, username):
		if username not in self.users:
			return 'User not found'
		user = self.users[username]
		notifications = []
		for transaction in user.bank_account.transactions:
			if transaction.amount > 500:
				notifications.append('Large transaction alert')
			if transaction.category == 'Bill' and transaction.date.day > 25:
				notifications.append('Upcoming bill payment alert')
		return notifications

	def send_alerts(self, username):
		if username not in self.users:
			return 'User not found'
		user = self.users[username]
		alerts = []
		for transaction in user.bank_account.transactions:
			if transaction.amount > 1000:
				alerts.append('Potential fraud alert')
		return alerts

	def encrypt_password(self, password):
		# Simple Caesar cipher for encryption
		shift = 3
		encrypted_password = ''
		for char in password:
			encrypted_password += chr((ord(char) + shift - 97) % 26 + 97)
		return encrypted_password

	def conduct_security_audit(self, username):
		if username not in self.users:
			return 'User not found'
		user = self.users[username]
		for transaction in user.bank_account.transactions:
			if transaction.amount > 5000:
				return 'Unusual activity detected'
		return 'No unusual activity detected'
