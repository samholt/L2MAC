class User:
	users = []
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = []
		User.users.append(self)

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
		User.users.remove(self)
