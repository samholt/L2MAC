class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.following = []
		self.feed = []
		self.notifications = []

	def submit_recipe(self, recipe):
		if recipe.validate_recipe():
			self.submitted_recipes.append(recipe)
		return recipe.validate_recipe()

	def edit_recipe(self, recipe, name, ingredients, instructions, images, categories):
		if recipe in self.submitted_recipes:
			recipe.edit_recipe(name, ingredients, instructions, images, categories)
		return recipe in self.submitted_recipes

	def delete_recipe(self, recipe):
		if recipe in self.submitted_recipes:
			self.submitted_recipes.remove(recipe)
		return recipe in self.submitted_recipes

	def save_favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def rate_recipe(self, recipe, rating, review_text):
		from review import Review
		review = Review(self, rating, review_text)
		recipe.add_review(review)

	def follow_user(self, user):
		self.following.append(user)

	def unfollow_user(self, user):
		if user in self.following:
			self.following.remove(user)

	def update_feed(self):
		self.feed = []
		for user in self.following:
			self.feed.extend(user.submitted_recipes)
		self.feed.sort(key=lambda x: x.timestamp, reverse=True)

	def share_recipe(self, recipe, platform):
		# This is a mock function as we cannot interact with social media platforms
		return f'Shared {recipe.name} on {platform}!'

	def get_recommendations(self, all_recipes):
		# This is a simple recommendation system based on user's favorite recipes' categories
		favorite_categories = [category for recipe in self.favorite_recipes for category in recipe.categories]
		recommended_recipes = [recipe for recipe in all_recipes if any(category in recipe.categories for category in favorite_categories)]
		return recommended_recipes

	def receive_notifications(self, new_recipes):
		# User receives notifications for new recipes in their interest areas
		interest_areas = [category for recipe in self.favorite_recipes for category in recipe.categories]
		for recipe in new_recipes:
			if any(category in recipe.categories for category in interest_areas):
				self.notifications.append(f'New recipe: {recipe.name}')

