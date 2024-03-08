class User:
	def __init__(self, id, name, email, password, books=[], notifications=[]):
		self.id = id
		self.name = name
		self.email = email
		self.password = password
		self.books = books
		self.notifications = notifications

	@classmethod
	def create(cls, name, email, password):
		return cls(None, name, email, password)

	def authenticate(self, email, password):
		return self.email == email and self.password == password

	def update_info(self, name=None, email=None, password=None, books=None):
		if name is not None:
			self.name = name
		if email is not None:
			self.email = email
		if password is not None:
			self.password = password
		if books is not None:
			self.books = books

	def notify(self, message):
		self.notifications.append(message)
