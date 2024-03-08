class User:
	def __init__(self, id, username, email, password, profile_picture=None, bio=None, website=None, location=None):
		self.id = id
		self.username = username
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location

	def authenticate(self, password):
		return self.password == password

	def update_profile(self, profile_picture=None, bio=None, website=None, location=None):
		if profile_picture is not None:
			self.profile_picture = profile_picture
		if bio is not None:
			self.bio = bio
		if website is not None:
			self.website = website
		if location is not None:
			self.location = location
		return True
