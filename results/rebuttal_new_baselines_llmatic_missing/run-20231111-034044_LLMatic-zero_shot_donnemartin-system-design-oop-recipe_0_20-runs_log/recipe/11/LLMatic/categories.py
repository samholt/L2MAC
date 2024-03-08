class Category:
	def __init__(self, db):
		self.db = db

	def add_category(self, category_name, recipe_id):
		if category_name not in self.db.categories:
			self.db.categories[category_name] = []
		self.db.categories[category_name].append(recipe_id)

	def get_recipes_by_category(self, category_name):
		return self.db.categories.get(category_name, [])

	def remove_recipe_from_category(self, category_name, recipe_id):
		if category_name in self.db.categories and recipe_id in self.db.categories[category_name]:
			self.db.categories[category_name].remove(recipe_id)
