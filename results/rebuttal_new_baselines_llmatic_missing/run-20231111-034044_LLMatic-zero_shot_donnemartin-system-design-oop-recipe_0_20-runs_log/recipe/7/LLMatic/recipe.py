class Recipe:
	def __init__(self, name, ingredients, instructions, images, category):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.category = category

	# Mock database
	db = {}

	def submit_recipe(self):
		if self.validate_recipe():
			self.db[self.name] = self
			return True
		return False

	def edit_recipe(self, name, ingredients, instructions, images, category):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.images = images
		self.category = category
		return True

	def delete_recipe(self):
		if self.name in self.db:
			del self.db[self.name]
			return True
		return False

	def validate_recipe(self):
		if not self.name or not self.ingredients or not self.instructions:
			return False
		return True
