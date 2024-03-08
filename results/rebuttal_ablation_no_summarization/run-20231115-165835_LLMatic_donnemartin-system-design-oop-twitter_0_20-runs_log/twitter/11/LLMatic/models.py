class User:
	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

users_db = {}

class Post:
	def __init__(self, post_id, user, content, image):
		self.post_id = post_id
		self.user = user
		self.content = content
		self.image = image

posts_db = {}

class Like:
	def __init__(self, like_id, user, post):
		self.like_id = like_id
		self.user = user
		self.post = post

likes_db = {}

class Notification:
	def __init__(self, notification_id, user, type, post):
		self.notification_id = notification_id
		self.user = user
		self.type = type
		self.post = post

	def view_notification(self):
		return {
			'notification_id': self.notification_id,
			'user': self.user.username,
			'type': self.type,
			'post': self.post.post_id
		}

notifications_db = {}

