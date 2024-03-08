from database import MockDatabase
from collections import Counter

class RecommendationManager:
	def __init__(self, db):
		self.db = db

	def get_recommendations(self, user_id):
		user = self.db.get_user(user_id)
		if not user:
			return []

		# Get all recipes from users that the current user is following
		following_recipes = [recipe for user_id in user.following for recipe in self.db.recipes.values() if recipe['user_id'] == user_id]

		# Get all categories from the recipes
		categories = [recipe['category'] for recipe in following_recipes]

		# Count the categories
		category_counter = Counter(categories)

		# Get the most common category
		most_common_category = category_counter.most_common(1)[0][0]

		# Get all recipes from the most common category
		recommended_recipes = [recipe for recipe in following_recipes if recipe['category'] == most_common_category]

		return recommended_recipes

