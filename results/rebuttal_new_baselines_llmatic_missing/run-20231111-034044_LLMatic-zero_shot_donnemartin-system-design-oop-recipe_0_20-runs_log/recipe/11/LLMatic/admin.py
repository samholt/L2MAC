from database import MockDatabase

db = MockDatabase()

def manage_recipes():
	return list(db.recipes.values())

def remove_content(recipe_id):
	if recipe_id in db.recipes:
		del db.recipes[recipe_id]
	return 'Recipe deleted successfully'

