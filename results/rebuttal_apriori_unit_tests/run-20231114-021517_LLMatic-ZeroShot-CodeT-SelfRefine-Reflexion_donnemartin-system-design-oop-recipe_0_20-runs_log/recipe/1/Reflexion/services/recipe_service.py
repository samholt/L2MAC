from models.recipe import Recipe

recipes_db = {}

class RecipeService:
	@staticmethod
	def create_recipe(recipe: Recipe):
		recipes_db[recipe.id] = recipe
		return recipe

	@staticmethod
	def get_recipe(recipe_id: str):
		return recipes_db.get(recipe_id)

	@staticmethod
	def update_recipe(recipe: Recipe):
		recipes_db[recipe.id] = recipe
		return recipe

	@staticmethod
	def delete_recipe(recipe_id: str):
		if recipe_id in recipes_db:
			del recipes_db[recipe_id]
