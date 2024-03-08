class User:
	users = {}

	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email

	@classmethod
	def create(cls, username, password, email):
		cls.users[username] = cls(username, password, email)
		return cls.users[username]

	@classmethod
	def exists(cls, username):
		return username in cls.users

	@classmethod
	def get(cls, username):
		return cls.users.get(username, None)

	@staticmethod
	def validate_password(username, password):
		user = User.get(username)
		if user:
			return user.password == password
		return False


class BankAccount:
	accounts = {}

	def __init__(self, user_id, bank_name, account_number):
		self.user_id = user_id
		self.bank_name = bank_name
		self.account_number = account_number

	@classmethod
	def link_account(cls, user_id, bank_name, account_number):
		cls.accounts[user_id] = cls(user_id, bank_name, account_number)
		return cls.accounts[user_id]

	@classmethod
	def unlink_account(cls, user_id):
		if user_id in cls.accounts:
			del cls.accounts[user_id]

	@classmethod
	def import_transactions(cls, user_id):
		# Mocking the import of transactions from a bank account
		return [{'id': 1, 'amount': 100, 'category': 'groceries', 'recurring': False}]
