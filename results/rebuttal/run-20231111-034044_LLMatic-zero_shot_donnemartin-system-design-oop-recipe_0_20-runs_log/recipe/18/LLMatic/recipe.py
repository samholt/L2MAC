class Recipe:
	def __init__(self, name, ingredients, instructions, images, categories):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.categories = categories
		# Mock database
		self.recipe_db = {}

	def submit_recipe(self):
		self.recipe_db[self.name] = {'ingredients': self.ingredients, 'instructions': self.instructions, 'images': self.images, 'categories': self.categories}
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

	def validate_recipe_format(self):
		if not self.name or not self.ingredients or not self.instructions or not self.images or not self.categories:
			return False
		return True

	def share_recipe(self, platform):
		return f'Recipe {self.name} shared on {platform}'
