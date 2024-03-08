class Recipe:
	def __init__(self, name, ingredients, instructions, images, categories):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.categories = categories

	def edit_recipe(self, name, ingredients, instructions, images, categories):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.categories = categories

	def delete_recipe(self):
		self.name = None
		self.ingredients = None
		self.instructions = None
		self.images = None
		self.categories = None


class RecipeValidator:
	@staticmethod
	def validate(recipe):
		if not recipe.name or not recipe.ingredients or not recipe.instructions:
			return False
		return True
