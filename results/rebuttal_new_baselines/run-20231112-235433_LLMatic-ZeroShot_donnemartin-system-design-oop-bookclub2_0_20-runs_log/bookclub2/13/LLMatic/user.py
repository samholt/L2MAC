class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.reading_list = []
		self.recommendations = []

	def create_user(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email

	def update_user(self, username=None, password=None, email=None):
		if username:
			self.username = username
		if password:
			self.password = password
		if email:
			self.email = email

	def delete_user(self):
		self.username = None
		self.password = None
		self.email = None
		self.reading_list = None
		self.recommendations = None
