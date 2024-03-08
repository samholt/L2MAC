import random

from user import User
from recipe import Recipe


class Recommendation:
	def __init__(self):
		self.users = {}
		self.recipes = {}

	def add_user(self, user: User):
		self.users[user.username] = user

	def add_recipe(self, recipe: Recipe):
		self.recipes[recipe.name] = recipe

	def generate_recommendations(self, username: str):
		user = self.users.get(username)
		if not user:
			return []

		# Get user preferences
		preferences = user.get_preferences()

		# Filter recipes based on user preferences
		recommended_recipes = [recipe for recipe in self.recipes.values() if recipe.category in preferences]

		# Shuffle the list to add randomness
		random.shuffle(recommended_recipes)

		return recommended_recipes[:10]

	def notify_user(self, username: str):
		recommended_recipes = self.generate_recommendations(username)
		if recommended_recipes:
			# Mocking the notification to user
			print(f'User {username} has been notified with new recipes.')
			return True
		return False
