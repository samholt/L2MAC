class Follow:
	def __init__(self):
		self.followers = {}

	def follow(self, follower, followee):
		if follower not in self.followers:
			self.followers[follower] = []
		self.followers[follower].append(followee)

	def get_followees(self, follower):
		return self.followers.get(follower, [])
