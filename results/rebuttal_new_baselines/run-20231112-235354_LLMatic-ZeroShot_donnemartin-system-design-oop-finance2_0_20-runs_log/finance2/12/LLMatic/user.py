class User:
	def __init__(self):
		self.users = {}

	def create_user(self, username, password):
		if username in self.users:
			return 'Username already exists'
		self.users[username] = {'password': password, 'details': {}, 'bank_accounts': []}
		return 'User created successfully'

	def login(self, username, password):
		if username not in self.users or self.users[username]['password'] != password:
			return 'Invalid username or password'
		return 'Logged in successfully'

	def update_details(self, username, details):
		if username not in self.users:
			return 'User not found'
		self.users[username]['details'] = details
		return 'Details updated successfully'

	def add_bank_account(self, username, bank_account):
		if username not in self.users:
			return 'User not found'
		self.users[username]['bank_accounts'].append(bank_account)
		return 'Bank account added successfully'
