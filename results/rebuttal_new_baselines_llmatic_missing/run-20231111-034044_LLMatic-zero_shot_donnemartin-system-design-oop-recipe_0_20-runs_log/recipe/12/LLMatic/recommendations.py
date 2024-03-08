from users import User, get_user
from recipes import Recipe


class Recommendations:
	def __init__(self):
		self.recommendations = {}
		self.notifications = {}

	def generate_recommendations(self, username):
		user = get_user(username)
		if not user:
			self.recommendations[username] = []
			return []

		# Mock recommendation generation based on user preferences and past activity
		self.recommendations[username] = ['recipe1', 'recipe2', 'recipe3']
		return self.recommendations[username]

	def send_notifications(self, username, new_recipes):
		user = get_user(username)
		if not user:
			self.notifications[username] = []
			return []

		# Mock notification sending for new recipes in the user's interest areas
		self.notifications[username] = new_recipes

	def get_recommendations(self, username):
		if username not in self.recommendations:
			self.generate_recommendations(username)
		return self.recommendations.get(username, [])

	def get_notifications(self, username):
		return self.notifications.get(username, [])
