class User:
	def __init__(self, id, name, email, password):
		self.id = id
		self.name = name
		self.email = email
		self.password = password

	def create_user(self, id, name, email, password):
		self.id = id
		self.name = name
		self.email = email
		self.password = password
		return self

	def authenticate_user(self, email, password):
		if self.email == email and self.password == password:
			return True
		return False

	def update_user(self, name=None, email=None, password=None):
		if name is not None:
			self.name = name
		if email is not None:
			self.email = email
		if password is not None:
			self.password = password
		return self
