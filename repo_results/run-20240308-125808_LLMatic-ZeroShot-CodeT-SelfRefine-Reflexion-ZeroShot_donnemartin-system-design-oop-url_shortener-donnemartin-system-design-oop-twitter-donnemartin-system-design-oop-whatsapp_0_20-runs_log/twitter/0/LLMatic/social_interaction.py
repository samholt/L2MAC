class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content

class Timeline:
	def __init__(self, user):
		self.user = user
		self.posts = []

	def update(self, posts):
		for post in posts:
			if post.user.username in [user.username for user in self.user.following]:
				self.posts.append(post)

	def view(self):
		return self.posts

class Notification:
	def __init__(self, user, notification_type, post):
		self.user = user
		self.notification_type = notification_type
		self.post = post

class SocialInteraction:
	def __init__(self):
		pass

