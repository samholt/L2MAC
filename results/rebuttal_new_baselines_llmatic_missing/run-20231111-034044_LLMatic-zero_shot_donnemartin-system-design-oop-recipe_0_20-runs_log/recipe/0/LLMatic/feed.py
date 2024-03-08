class Feed:
	def __init__(self, user):
		self.user = user

	def generate_feed(self):
		feed = []
		for followed_user in self.user.followed_users:
			feed.extend(followed_user.get_recent_activity())
		feed.sort(key=lambda x: x['timestamp'], reverse=True)
		return feed
