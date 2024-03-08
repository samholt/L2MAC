class Recipe:
	def __init__(self, name, ingredients, instructions, images, categories):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.categories = categories

	def edit_recipe(self, name=None, ingredients=None, instructions=None, images=None, categories=None):
		if name:
			self.name = name
		if ingredients:
			self.ingredients = ingredients
		if instructions:
			self.instructions = instructions
		if images:
			self.images = images
		if categories:
			self.categories = categories

	def delete_recipe(self):
		self.name = None
		self.ingredients = None
		self.instructions = None
		self.images = None
		self.categories = None
