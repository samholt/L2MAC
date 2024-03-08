from models import User


class Auth:
	def __init__(self):
		self.logged_in_user = None

	def login(self, username, password):
		if User.validate_password(username, password):
			self.logged_in_user = username
			return True
		return False

	def logout(self):
		self.logged_in_user = None

	def register(self, username, password, email):
		if not User.user_exists(username):
			new_user = User.create_user(username, password, email)
			# Here we should add the new user to the database
			# But as we are mocking the database, we are not doing it
			return True
		return False
