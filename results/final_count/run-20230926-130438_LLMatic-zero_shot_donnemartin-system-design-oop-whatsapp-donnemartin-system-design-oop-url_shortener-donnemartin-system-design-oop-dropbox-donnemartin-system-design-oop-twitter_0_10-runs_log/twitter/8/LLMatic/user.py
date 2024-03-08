import hashlib


class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password = self._hash_password(password)
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.following = []
		self.followers = []
		self.blocked_users = []

	def _hash_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def register(self):
		# Mock database
		db = {}
		db[self.username] = {
			'email': self.email,
			'username': self.username,
			'password': self.password,
			'profile_picture': self.profile_picture,
			'bio': self.bio,
			'website_link': self.website_link,
			'location': self.location
		}
		return db[self.username]

	def reset_password(self, new_password):
		self.password = self._hash_password(new_password)
		return self.password

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		self.profile_picture = profile_picture if profile_picture else self.profile_picture
		self.bio = bio if bio else self.bio
		self.website_link = website_link if website_link else self.website_link
		self.location = location if location else self.location
		return {'profile_picture': self.profile_picture, 'bio': self.bio, 'website_link': self.website_link, 'location': self.location}

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)
		return self.following

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)
		return self.following

	def block_user(self, user):
		if user not in self.blocked_users:
			self.blocked_users.append(user)
		return self.blocked_users

	def unblock_user(self, user):
		if user in self.blocked_users:
			self.blocked_users.remove(user)
		return self.blocked_users
