class Recommendation:
	def __init__(self, users, recipes):
		self.users = users
		self.recipes = recipes.recipes

	def recommend(self, user_id):
		user = self.users.get_user(user_id)
		if not user:
			return {'error': 'User not found'}, 404

		# Recommend recipes based on the categories of recipes the user has liked
		liked_categories = [recipe['category'] for recipe in user.liked_recipes]
		recommendations = [recipe for recipe in self.recipes.values() if recipe['category'] in liked_categories]

		return recommendations, 200
