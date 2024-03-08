class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.following = []
		self.feed = []

	def create_account(self, username, password):
		self.username = username
		self.password = password

	def manage_account(self, username, password):
		self.username = username
		self.password = password

	def save_favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def submit_recipe(self, recipe):
		self.submitted_recipes.append(recipe)

	def follow_user(self, user):
		self.following.append(user)

	def update_feed(self):
		for user in self.following:
			self.feed.extend(user.submitted_recipes)
		self.feed.sort(key=lambda x: x.timestamp, reverse=True)
		return self.feed

	def monitor_site_usage(self):
		user_engagement = len(self.following) + len(self.submitted_recipes) + len(self.favorite_recipes)
		return user_engagement

	def generate_recommendations(self):
		from recipe import Recipe
		interest_areas = [recipe.category for recipe in self.favorite_recipes + self.submitted_recipes]
		recommendations = [recipe for recipe in Recipe.recipe_db.values() if recipe.category in interest_areas]
		return recommendations

	def receive_notifications(self):
		from recipe import Recipe
		interest_areas = [recipe.category for recipe in self.favorite_recipes + self.submitted_recipes]
		new_recipes = [recipe for recipe in Recipe.recipe_db.values() if recipe.category in interest_areas and recipe not in self.feed + self.favorite_recipes + self.submitted_recipes]
		self.feed.extend(new_recipes)
		return new_recipes if new_recipes else 'No new recipes'
