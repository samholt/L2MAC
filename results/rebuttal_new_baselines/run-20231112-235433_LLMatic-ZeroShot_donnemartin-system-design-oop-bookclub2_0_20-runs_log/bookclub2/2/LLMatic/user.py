class User:
	def __init__(self, id, name, email, password):
		self.id = id
		self.name = name
		self.email = email
		self.password = password

	@staticmethod
	def create_user(id, name, email, password):
		return User(id, name, email, password)

	def authenticate(self, email, password):
		return self.email == email and self.password == password

	def get_info(self):
		return {
			'id': self.id,
			'name': self.name,
			'email': self.email
		}
