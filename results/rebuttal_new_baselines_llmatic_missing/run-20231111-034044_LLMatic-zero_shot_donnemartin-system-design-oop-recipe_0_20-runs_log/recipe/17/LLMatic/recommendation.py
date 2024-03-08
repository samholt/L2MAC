class Recommendation:
	def __init__(self):
		self.user_preferences = {}
		self.user_activity = {}
		self.notifications = {}

	def set_user_preferences(self, user_id, preferences):
		self.user_preferences[user_id] = preferences

	def track_user_activity(self, user_id, activity):
		if user_id not in self.user_activity:
			self.user_activity[user_id] = []
		self.user_activity[user_id].append(activity)

	def generate_recommendations(self, user_id):
		# Mock database of recipes
		mock_db = {}
		recommendations = []
		for recipe_id, recipe in mock_db.items():
			if any(category in recipe.categories for category in self.user_preferences[user_id]):
				recommendations.append(recipe_id)
		return recommendations

	def notify_user(self, user_id, new_recipes):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].extend(new_recipes)
