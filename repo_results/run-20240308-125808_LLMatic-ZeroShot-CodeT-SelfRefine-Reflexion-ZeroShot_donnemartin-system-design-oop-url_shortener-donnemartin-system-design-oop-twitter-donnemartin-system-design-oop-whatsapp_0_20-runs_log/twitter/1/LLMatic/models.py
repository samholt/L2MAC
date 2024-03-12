class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.followers = []
		self.following = []

	def reset_password(self, new_password):
		self.password = new_password

	def update_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		if profile_picture is not None:
			self.profile_picture = profile_picture
		if bio is not None:
			self.bio = bio
		if website_link is not None:
			self.website_link = website_link
		if location is not None:
			self.location = location

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)


class Post:
	def __init__(self, text, images, user):
		self.text = text
		self.images = images
		self.user = user
		self.likes = []
		self.retweets = []
		self.replies = []

	def like(self, user):
		self.likes.append(user)

	def retweet(self, user):
		self.retweets.append(user)

	def reply(self, user, text):
		self.replies.append({'user': user, 'text': text})


class Message:
	def __init__(self, sender, receiver, text):
		self.sender = sender
		self.receiver = receiver
		self.text = text
