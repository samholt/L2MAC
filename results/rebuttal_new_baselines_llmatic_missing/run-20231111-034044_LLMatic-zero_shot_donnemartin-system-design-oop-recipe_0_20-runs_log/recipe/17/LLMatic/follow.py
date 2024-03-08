class Follow:
	def __init__(self):
		self.follows = {}

	def follow(self, follower_id, followee_id):
		if follower_id not in self.follows:
			self.follows[follower_id] = set()
		self.follows[follower_id].add(followee_id)

	def unfollow(self, follower_id, followee_id):
		if follower_id in self.follows and followee_id in self.follows[follower_id]:
			self.follows[follower_id].remove(followee_id)

	def get_followees(self, follower_id):
		if follower_id in self.follows:
			return self.follows[follower_id]
		return set()
