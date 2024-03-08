class User:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.is_authenticated = False

	def signup(self, email, password):
		# In a real system, we would save these details in a database
		self.email = email
		self.password = password
		return True

	def login(self, email, password):
		# In a real system, we would check these details against a database
		if self.email == email and self.password == password:
			self.is_authenticated = True
			return True
		return False

	def recover_password(self, email):
		# In a real system, we would send a password recovery email
		if self.email == email:
			return 'Password recovery email sent'
		return 'Email not found'

