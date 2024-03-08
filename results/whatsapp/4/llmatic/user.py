class User:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.statuses = []
		self.contacts = []
		# other attributes...
