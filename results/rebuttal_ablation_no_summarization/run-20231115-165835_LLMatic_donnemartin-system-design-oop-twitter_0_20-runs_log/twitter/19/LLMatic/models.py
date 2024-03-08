class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None, is_private=False):
		self.email = email
		self.username = username
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.is_private = is_private
		self.is_authenticated = False

	def authenticate(self, password):
		if self.password == password:
			self.is_authenticated = True
		return self.is_authenticated


class Post:
	def __init__(self, user, text_content, images=None):
		self.user = user
		self.text_content = text_content
		self.images = images if images else []
