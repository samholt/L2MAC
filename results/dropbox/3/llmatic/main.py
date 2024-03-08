import user
import file
import folder
import permission
import shared_file


class Application:
	def __init__(self):
		self.users = {}
		self.sessions = {}

	def register(self, username, password):
		if username not in self.users:
			new_user = user.User(username, password)
			self.users[username] = new_user
			return 'Registration successful'
		else:
			return 'Username already exists'

	def login(self, username, password):
		if username in self.users and self.users[username].password == password:
			self.sessions[username] = True
			return 'Login successful'
		else:
			return 'Invalid username or password'

	def logout(self, username):
		if username in self.sessions:
			del self.sessions[username]
			return 'Logout successful'
		else:
			return 'User not logged in'

	def is_logged_in(self, username):
		return self.sessions.get(username, False)

