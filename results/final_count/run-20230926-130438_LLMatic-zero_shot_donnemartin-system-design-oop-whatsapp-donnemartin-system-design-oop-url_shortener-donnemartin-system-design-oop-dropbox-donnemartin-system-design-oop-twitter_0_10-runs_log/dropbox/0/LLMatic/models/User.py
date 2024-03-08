class User:
	def __init__(self, id, name, email, password, profile_picture, storage_used):
		self.id = id
		self.name = name
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.storage_used = storage_used

	def __repr__(self):
		return f'User({self.id}, {self.name}, {self.email}, {self.password}, {self.profile_picture}, {self.storage_used})'

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'email': self.email,
			'password': self.password,
			'profile_picture': self.profile_picture,
			'storage_used': self.storage_used
		}
