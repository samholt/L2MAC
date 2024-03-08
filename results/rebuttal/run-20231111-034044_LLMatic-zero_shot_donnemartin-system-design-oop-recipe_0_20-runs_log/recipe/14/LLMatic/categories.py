class Categories:
	def __init__(self):
		self.categories = {'type': [], 'cuisine': [], 'dietary': []}

	def add_category(self, category_type, category):
		if category not in self.categories[category_type]:
			self.categories[category_type].append(category)

	def get_categories(self, category_type):
		return self.categories[category_type]

	def categorize_recipe(self, recipe_id, category_type, category):
		if category in self.categories[category_type]:
			return {'recipe_id': recipe_id, 'category_type': category_type, 'category': category}
		else:
			return 'Category does not exist'
