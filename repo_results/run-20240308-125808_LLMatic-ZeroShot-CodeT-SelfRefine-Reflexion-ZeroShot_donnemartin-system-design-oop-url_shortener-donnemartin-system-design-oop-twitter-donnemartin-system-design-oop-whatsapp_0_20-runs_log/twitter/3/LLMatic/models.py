class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location

	def reset_password(self, new_password):
		self.password = new_password

	def update_profile(self, profile_picture, bio, website_link, location):
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location

	def to_dict(self):
		return {
			'email': self.email,
			'username': self.username,
			'profile_picture': self.profile_picture,
			'bio': self.bio,
			'website_link': self.website_link,
			'location': self.location
		}

class Post:
	def __init__(self, user, text, images):
		self.user = user
		self.text = text
		self.images = images
		self.likes = []
		self.retweets = []
		self.replies = []

	def like(self, user):
		self.likes.append(user)

	def retweet(self, user):
		self.retweets.append(user)

	def reply(self, user, text):
		self.replies.append({'user': user, 'text': text})

	def to_dict(self):
		return {
			'user': self.user.to_dict(),
			'text': self.text,
			'images': self.images,
			'likes': [user.to_dict() for user in self.likes],
			'retweets': [user.to_dict() for user in self.retweets],
			'replies': [{'user': reply['user'].to_dict(), 'text': reply['text']} for reply in self.replies]
		}

# Mock database
users_db = {}
posts_db = {}
likes_db = {}
retweets_db = {}
replies_db = {}
