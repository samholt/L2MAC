class Community:
	def __init__(self):
		self.following = {}
		self.feed = {}

	def follow(self, user_id, follow_id):
		if user_id not in self.following:
			self.following[user_id] = []
		self.following[user_id].append(follow_id)

	def generate_feed(self, user_id):
		if user_id in self.following:
			for follow_id in self.following[user_id]:
				if follow_id in self.feed:
					self.feed[user_id] = self.feed[follow_id]

	def share_recipe(self, user_id, recipe_id, platform):
		return f'User {user_id} shared recipe {recipe_id} on {platform}'
