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


class Post:
	def __init__(self, id, user_id, content, timestamp):
		self.id = id
		self.user_id = user_id
		self.content = content
		self.timestamp = timestamp
