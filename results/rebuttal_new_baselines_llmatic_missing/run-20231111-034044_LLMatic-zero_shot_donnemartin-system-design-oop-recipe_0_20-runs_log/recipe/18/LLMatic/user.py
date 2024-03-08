class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.followed_users = []
		self.recommendations = []
		self.notifications = []

	def create_account(self, username, password):
		self.username = username
		self.password = password

	def save_favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def submit_recipe(self, recipe):
		self.submitted_recipes.append(recipe)

	def follow_user(self, user_to_follow):
		self.followed_users.append(user_to_follow)

	def view_feed(self):
		feed = []
		for user in self.followed_users:
			feed.extend(user.submitted_recipes)
		return feed

	def generate_recommendations(self):
		# Mock recommendation generation based on user's favorite recipes
		self.recommendations = self.favorite_recipes

	def receive_notifications(self, new_recipe):
		self.notifications.append(new_recipe)
