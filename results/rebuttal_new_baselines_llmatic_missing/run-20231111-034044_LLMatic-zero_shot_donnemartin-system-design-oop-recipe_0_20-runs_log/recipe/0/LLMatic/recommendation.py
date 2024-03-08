class Recommendation:
	def __init__(self, users, recipes):
		self.users = users
		self.recipes = recipes

	def generate_recommendations(self, user_id):
		user = self.users.get(user_id)
		if user is None:
			return []
		recommended_recipes = []
		for recipe in self.recipes:
			if recipe.category in user.favorite_recipes:
				recommended_recipes.append(recipe)
		return recommended_recipes

	def notify_user(self, user_id):
		user = self.users.get(user_id)
		if user is None:
			return
		recommended_recipes = self.generate_recommendations(user_id)
		user.notifications.extend(recommended_recipes)
