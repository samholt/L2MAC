class Recommendation:
	def __init__(self):
		self.user_preferences = {}
		self.user_activity = {}
		self.recipe_database = {}

	def generate_recommendations(self, user_id):
		user_pref = self.user_preferences.get(user_id, [])
		user_act = self.user_activity.get(user_id, [])
		recommendations = []
		for recipe in self.recipe_database.values():
			if recipe['category'] in user_pref and recipe['id'] not in user_act:
				recommendations.append(recipe)
		return recommendations

	def notify_user(self, user_id, new_recipes):
		user_pref = self.user_preferences.get(user_id, [])
		for recipe in new_recipes:
			if recipe['category'] in user_pref:
				print(f'New recipe in your interest area: {recipe}')
