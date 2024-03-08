class Category:
	def __init__(self):
		self.categories = {}

	def add_category(self, category_type, category_name):
		if category_type not in self.categories:
			self.categories[category_type] = []
		self.categories[category_type].append(category_name)

	def get_categories(self, category_type):
		return self.categories.get(category_type, [])

	def categorize_recipe(self, recipe_id, category_type, category_name):
		if category_type not in self.categories or category_name not in self.categories[category_type]:
			return 'Invalid category'
		return 'Recipe categorized successfully'
