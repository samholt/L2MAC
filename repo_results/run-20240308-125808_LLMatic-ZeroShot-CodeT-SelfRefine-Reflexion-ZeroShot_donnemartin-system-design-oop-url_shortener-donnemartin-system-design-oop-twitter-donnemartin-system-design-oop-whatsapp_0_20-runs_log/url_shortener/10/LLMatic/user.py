class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = []

	def create_user(self, username, password):
		self.username = username
		self.password = password

	def edit_user(self, username, password):
		self.username = username
		self.password = password

	def delete_user(self):
		self.username = None
		self.password = None
		self.urls = []