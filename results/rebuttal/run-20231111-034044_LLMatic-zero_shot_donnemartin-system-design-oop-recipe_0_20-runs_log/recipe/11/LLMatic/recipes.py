from database import MockDatabase

class RecipeManager:
	def __init__(self, db):
		self.db = db

	def submit_recipe(self, recipe_id, user_id, title, description, ingredients, category):
		if recipe_id in self.db.recipes:
			return 'Recipe already exists'
		recipe = {'recipe_id': recipe_id, 'user_id': user_id, 'title': title, 'description': description, 'ingredients': ingredients, 'category': category}
		self.db.add_recipe(recipe)
		return recipe

	def get_recipe(self, recipe_id):
		return self.db.recipes.get(recipe_id, 'Recipe not found')

	def edit_recipe(self, recipe_id, title=None, description=None, ingredients=None, category=None):
		if recipe_id not in self.db.recipes:
			return 'Recipe not found'
		if title is not None:
			self.db.recipes[recipe_id]['title'] = title
		if description is not None:
			self.db.recipes[recipe_id]['description'] = description
		if ingredients is not None:
			self.db.recipes[recipe_id]['ingredients'] = ingredients
		if category is not None:
			self.db.recipes[recipe_id]['category'] = category
		return 'Recipe edited successfully'

	def delete_recipe(self, recipe_id):
		if recipe_id not in self.db.recipes:
			return 'Recipe not found'
		del self.db.recipes[recipe_id]
		return 'Recipe deleted successfully'

	def search_recipes(self, search_term):
		results = {}
		for recipe_id, recipe in self.db.recipes.items():
			if search_term in recipe['title'] or search_term in recipe['ingredients'] or search_term in recipe['category']:
				results[recipe_id] = recipe
		return results

	def get_all_recipes(self):
		return self.db.recipes
