import hashlib

# Mock database
users_db = {}


class User:
	def __init__(self, username, password):
		self.username = username
		self.password = self._encrypt_password(password)

	def _encrypt_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def check_password(self, password):
		return self.password == self._encrypt_password(password)


def create_user(username, password):
	if username in users_db:
		return False
	users_db[username] = User(username, password)
	return True


def login(username, password):
	if username not in users_db:
		return False
	user = users_db[username]
	return user.check_password(password)


def recover_password(username):
	if username not in users_db:
		return None
	user = users_db[username]
	return user.password
