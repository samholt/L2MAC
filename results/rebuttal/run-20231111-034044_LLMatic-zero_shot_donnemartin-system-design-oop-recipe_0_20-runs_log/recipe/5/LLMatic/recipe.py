class Recipe:
	def __init__(self, name, ingredients, instructions, images, category):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.category = category
		# Mock database
		self.recipe_db = {}
		self.ratings = []

	def submit_recipe(self):
		self.recipe_db[self.name] = {'name': self.name, 'ingredients': self.ingredients, 'instructions': self.instructions, 'images': self.images, 'category': self.category}
		return 'Recipe submitted successfully'

	def edit_recipe(self, new_recipe):
		if self.name in self.recipe_db:
			self.recipe_db[self.name] = new_recipe
			return 'Recipe edited successfully'
		else:
			return 'Recipe not found'

	def delete_recipe(self):
		if self.name in self.recipe_db:
			del self.recipe_db[self.name]
			return 'Recipe deleted successfully'
		else:
			return 'Recipe not found'

	def validate_recipe(self):
		if not self.name or not self.ingredients or not self.instructions or not self.images or not self.category:
			return False
		return True

	def search_recipe(self, search_term):
		results = {}
		for recipe in self.recipe_db.values():
			if search_term in recipe['ingredients'] or search_term in recipe['name'] or search_term in recipe['category']:
				results[recipe['name']] = recipe
		return results

	def categorize_recipe(self, category):
		results = {}
		for recipe in self.recipe_db.values():
			if category in recipe['category']:
				results[recipe['name']] = recipe
		return results

	def add_rating(self, rating):
		self.ratings.append(rating)

	def calculate_average_rating(self):
		if self.ratings:
			return sum(self.ratings) / len(self.ratings)
		else:
			return 'No ratings yet'

	def recommend_recipes(self, user):
		# Recommend recipes based on user's favorite recipes' categories
		recommended_recipes = {}
		for favorite_recipe in user.favorite_recipes:
			for recipe in self.recipe_db.values():
				if favorite_recipe.category == recipe['category'] and recipe['name'] not in [fav_recipe.name for fav_recipe in user.favorite_recipes] and recipe['name'] not in user.seen_recipes:
					recommended_recipes[recipe['name']] = recipe
					user.seen_recipes.append(recipe['name'])
		return recommended_recipes

	def notify_new_recipes(self, user):
		# Notify user of new recipes in their favorite categories
		new_recipes = {}
		for favorite_recipe in user.favorite_recipes:
			for recipe in self.recipe_db.values():
				if favorite_recipe.category == recipe['category'] and recipe['name'] not in [recipe.name for recipe in user.submitted_recipes] and recipe['name'] not in user.seen_recipes:
					new_recipes[recipe['name']] = recipe
					user.seen_recipes.append(recipe['name'])
		return new_recipes

	def to_dict(self):
		return {
			'name': self.name,
			'ingredients': self.ingredients,
			'instructions': self.instructions,
			'images': self.images,
			'category': self.category
		}
