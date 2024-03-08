class AuthService:
	def __init__(self):
		self.users = {}

	def sign_up(self, email, password):
		if email in self.users:
			return False
		self.users[email] = {'password': password}
		return True

	def recover_password(self, email):
		if email not in self.users:
			return False
		# In a real-world application, the password would be sent to the user's email.
		# Here, we just return True to indicate that the process was successful.
		return True
