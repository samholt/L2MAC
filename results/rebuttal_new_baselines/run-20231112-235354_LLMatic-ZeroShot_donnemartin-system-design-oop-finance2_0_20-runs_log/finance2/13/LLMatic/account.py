class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.linked_bank_accounts = []
		self.auth_code = None

	def create_user(self, username, password):
		# Create a new user
		self.username = username
		self.password = password

	def authenticate_user(self, username, password, auth_code):
		# Authenticate the user
		if self.username == username and self.password == password and self.auth_code == auth_code:
			return True
		return False

	def link_bank_account(self, account_number):
		# Link a bank account
		self.linked_bank_accounts.append(account_number)

	def send_auth_code(self, email):
		# Mock sending email
		self.auth_code = '123456'
		return self.auth_code
