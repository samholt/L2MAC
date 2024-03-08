class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.following = []
		self.activity_feed = []
		self.seen_recipes = []

	def submit_recipe(self, recipe):
		self.submitted_recipes.append(recipe)

	def favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def remove_favorite_recipe(self, recipe):
		if recipe in self.favorite_recipes:
			self.favorite_recipes.remove(recipe)

	def change_password(self, new_password):
		self.password = new_password

	def follow_user(self, user):
		if user not in self.following:
			self.following.append(user)

	def unfollow_user(self, user):
		if user in self.following:
			self.following.remove(user)

	def update_activity_feed(self):
		self.activity_feed = []
		for user in self.following:
			self.activity_feed.extend(user.submitted_recipes)
		self.activity_feed.sort(key=lambda x: x['timestamp'], reverse=True)


class Profile:
	def __init__(self, user):
		self.user = user

	def display_submitted_recipes(self):
		return self.user.submitted_recipes

	def display_favorite_recipes(self):
		return self.user.favorite_recipes

	def display_following(self):
		return self.user.following

	def display_activity_feed(self):
		self.user.update_activity_feed()
		return self.user.activity_feed
