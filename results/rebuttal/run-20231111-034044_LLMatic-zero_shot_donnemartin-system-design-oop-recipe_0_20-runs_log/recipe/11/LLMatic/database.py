class MockDatabase:
	def __init__(self):
		self.users = {}
		self.recipes = {}
		self.reviews = {}
		self.categories = {}

	def add_user(self, user):
		self.users[user.id] = user

	def add_recipe(self, recipe):
		self.recipes[recipe['recipe_id']] = recipe

	def add_review(self, review):
		self.reviews[review['recipe_id']] = review

	def add_category(self, category):
		self.categories[category['category_name']] = category

	def get_user(self, user_id):
		user = self.users.get(user_id)
		if user:
			from users import User
			return User(user.id, user.name, user.email, user.following)
		return None

	def get_recipe(self, recipe_id):
		return self.recipes.get(recipe_id)

	def get_reviews(self, recipe_id):
		return self.reviews.get(recipe_id)

	def get_category(self, category_name):
		return self.categories.get(category_name)

	def get_all_recipes(self):
		return list(self.recipes.values())

	def delete_recipe(self, recipe_id):
		if recipe_id in self.recipes:
			del self.recipes[recipe_id]
			return 'Recipe deleted successfully'
		return 'Recipe not found'

	def get_recommendations(self, user_id):
		if user_id in self.users:
			return []
		return 'User not found'
