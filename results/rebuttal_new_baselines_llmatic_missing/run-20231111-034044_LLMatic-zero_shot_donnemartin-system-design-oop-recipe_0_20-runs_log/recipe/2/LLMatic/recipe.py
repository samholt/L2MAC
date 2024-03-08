class Recipe:
	def __init__(self, name, ingredients, instructions, images, category, type, cuisine, diet):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.category = category
		self.type = type
		self.cuisine = cuisine
		self.diet = diet

	# Mock database
	recipe_db = {}

	def submit_recipe(self):
		self.recipe_db[self.name] = self
		return 'Recipe submitted successfully'

	def edit_recipe(self, name, ingredients, instructions, images, category, type, cuisine, diet):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.category = category
		self.type = type
		self.cuisine = cuisine
		self.diet = diet
		return 'Recipe edited successfully'

	def delete_recipe(self):
		if self.name in self.recipe_db:
			del self.recipe_db[self.name]
			return 'Recipe deleted successfully'
		else:
			return 'Recipe not found'

	def validate_recipe_format(self):
		if not self.name or not self.ingredients or not self.instructions or not self.images or not self.category or not self.type or not self.cuisine or not self.diet:
			return False
		return True
