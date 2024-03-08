from models import User, BankAccount
import random
import string

class UserService:
	def __init__(self):
		self.users = {}
		self.otps = {}

	def create_user(self, username, password, email):
		user = User(username, password, email)
		self.users[username] = user
		return user

	def update_user(self, username, new_password, new_email):
		if username in self.users:
			user = self.users[username]
			user.password = new_password
			user.email = new_email
			return user
		return None

	def delete_user(self, username):
		if username in self.users:
			del self.users[username]
			return True
		return False

	def generate_otp(self, username):
		if username in self.users:
			otp = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
			self.otps[username] = otp
			return otp
		return None

	def verify_otp(self, username, otp):
		if username in self.users and username in self.otps:
			if self.otps[username] == otp:
				del self.otps[username]
				return True
		return False

class BankAccountService:
	def __init__(self):
		self.bank_accounts = {}

	def link_bank_account(self, account_number, bank_name, user_id):
		bank_account = BankAccount(account_number, bank_name, user_id)
		self.bank_accounts[account_number] = bank_account
		return bank_account

	def update_bank_account(self, account_number, new_bank_name):
		if account_number in self.bank_accounts:
			bank_account = self.bank_accounts[account_number]
			bank_account.bank_name = new_bank_name
			return bank_account
		return None

	def unlink_bank_account(self, account_number):
		if account_number in self.bank_accounts:
			del self.bank_accounts[account_number]
			return True
		return False
