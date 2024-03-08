class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.following = []
		self.feed = []
		self.preferences = []
		self.notifications = []

	def create_account(self, username, password):
		self.username = username
		self.password = password

	def manage_account(self, username, password):
		self.username = username
		self.password = password

	def save_favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def follow_user(self, user):
		self.following.append(user)
		self.update_feed(user)

	def update_feed(self, user):
		for recipe in user.submitted_recipes:
			self.feed.append(recipe)

	def set_preferences(self, preferences):
		self.preferences = preferences

	def generate_recommendations(self):
		# Mocking the recommendation generation process
		return ['recipe1', 'recipe2', 'recipe3']

	def receive_notification(self, notification):
		self.notifications.append(notification)
