from werkzeug.security import generate_password_hash, check_password_hash

class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password_hash = generate_password_hash(password)
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def reset_password(self, new_password):
		self.password_hash = generate_password_hash(new_password)

	def update_profile(self, profile_picture, bio, website_link, location):
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		return self

