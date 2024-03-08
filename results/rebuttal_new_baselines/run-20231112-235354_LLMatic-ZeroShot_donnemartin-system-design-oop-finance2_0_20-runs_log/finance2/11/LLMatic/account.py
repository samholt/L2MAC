class User:
	def __init__(self):
		self.users = {}

	def create_account(self, username, password):
		if username in self.users:
			return 'Username already exists'
		self.users[username] = {'password': password, 'bank_account': None}
		return 'Account created successfully'

	def link_bank_account(self, username, bank_account):
		for user in self.users.values():
			if user['bank_account'] == bank_account:
				return 'Bank account already linked to another user'
		if username in self.users:
			self.users[username]['bank_account'] = bank_account
			return 'Bank account linked successfully'
		return 'User not found'

	def handle_authentication(self, username, password):
		if username in self.users and self.users[username]['password'] == password:
			return 'Authentication successful'
		return 'Authentication failed'
