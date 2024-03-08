class Recipe:
	def __init__(self):
		self.recipes = {}

	def submit_recipe(self, recipe_id, recipe):
		self.recipes[recipe_id] = recipe
		return {'status': 'Recipe submitted successfully'}

	def get_recipe(self, recipe_id):
		if recipe_id in self.recipes:
			return self.recipes[recipe_id]
		else:
			return {'error': 'Recipe not found'}

	def edit_recipe(self, recipe_id, updated_recipe):
		if recipe_id in self.recipes:
			self.recipes[recipe_id] = updated_recipe
			return {'status': 'Recipe updated successfully'}
		else:
			return {'error': 'Recipe not found'}

	def delete_recipe(self, recipe_id):
		if recipe_id in self.recipes:
			del self.recipes[recipe_id]
			return {'status': 'Recipe deleted successfully'}
		else:
			return {'error': 'Recipe not found'}

	def search_by_ingredients(self, ingredients):
		results = [recipe for recipe in self.recipes.values() if all(ingredient in recipe['ingredients'] for ingredient in ingredients)]
		return results

	def search_by_name(self, name):
		results = [recipe for recipe in self.recipes.values() if name.lower() in recipe['name'].lower()]
		return results

	def search_by_category(self, category):
		results = [recipe for recipe in self.recipes.values() if category.lower() in recipe['category'].lower()]
		return results
