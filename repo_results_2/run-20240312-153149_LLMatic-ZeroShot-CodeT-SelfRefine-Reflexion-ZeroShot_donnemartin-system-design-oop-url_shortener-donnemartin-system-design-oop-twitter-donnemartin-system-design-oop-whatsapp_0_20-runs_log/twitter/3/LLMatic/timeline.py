class Timeline:
	def __init__(self, user):
		self.user = user
		self.posts = []

	def get_timeline_posts(self):
		for user in self.user.following:
			self.posts.extend(user.posts)
		self.posts.sort(key=lambda x: x.timestamp, reverse=True)
		return self.posts
