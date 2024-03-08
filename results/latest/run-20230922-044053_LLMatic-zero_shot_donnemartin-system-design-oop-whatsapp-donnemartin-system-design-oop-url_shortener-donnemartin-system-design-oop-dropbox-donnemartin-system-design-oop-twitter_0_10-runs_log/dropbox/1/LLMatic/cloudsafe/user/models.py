from werkzeug.security import generate_password_hash, check_password_hash


class User:
	def __init__(self, name, email, password, profile_picture=None, storage_used=0, storage_remaining=100):
		self.name = name
		self.email = email
		self.password_hash = generate_password_hash(password)
		self.profile_picture = profile_picture
		self.storage_used = storage_used
		self.storage_remaining = storage_remaining

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def update_profile(self, name=None, email=None, password=None, profile_picture=None):
		if name:
			self.name = name
		if email:
			self.email = email
		if password:
			self.password_hash = generate_password_hash(password)
		if profile_picture:
			self.profile_picture = profile_picture
