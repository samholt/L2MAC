import hashlib
class User:
	def __init__(self, id, name, email, password, profile_picture, storage_used):
		self.id = id
		self.name = name
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.storage_used = storage_used

	def check_password(self, password):
		return self.password == hashlib.sha256(password.encode()).hexdigest()
