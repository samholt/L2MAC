from user import User
from recipe import Recipe
from review import Review

class Admin(User):
	def __init__(self, username, password):
		super().__init__(username, password)

	def manage_recipes(self, recipe):
		if recipe in Recipe.recipe_db.values():
			Recipe.recipe_db.pop(recipe.instructions)
			return 'Recipe removed successfully'
		else:
			return 'Recipe not found'

	def remove_inappropriate_content(self, review):
		if review in Review.review_db.values():
			Review.review_db.pop((review.user, review.recipe))
			return 'Review removed successfully'
		else:
			return 'Review not found'
