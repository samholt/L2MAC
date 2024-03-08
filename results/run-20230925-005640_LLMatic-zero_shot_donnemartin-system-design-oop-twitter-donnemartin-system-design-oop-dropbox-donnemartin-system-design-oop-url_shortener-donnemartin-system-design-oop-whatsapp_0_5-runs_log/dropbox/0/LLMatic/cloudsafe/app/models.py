from werkzeug.security import generate_password_hash

class User:
	def __init__(self, id, name, email, password, profile_picture, storage_used):
		self.id = id
		self.name = name
		self.email = email
		self.password = self.set_password(password)
		self.profile_picture = profile_picture
		self.storage_used = storage_used

	def __repr__(self):
		return f'User({self.name}, {self.email})'

	def set_password(self, password):
		return generate_password_hash(password)

class File:
	def __init__(self, id, name, size, type, path, user_id, versions=None):
		self.id = id
		self.name = name
		self.size = size
		self.type = type
		self.path = path
		self.user_id = user_id
		self.versions = versions if versions else []

	def __repr__(self):
		return f'File({self.name}, {self.size}, {self.type}, {self.path}, {self.user_id})'

class Folder:
	def __init__(self, id, name, user_id):
		self.id = id
		self.name = name
		self.user_id = user_id

	def __repr__(self):
		return f'Folder({self.name}, {self.user_id})'
