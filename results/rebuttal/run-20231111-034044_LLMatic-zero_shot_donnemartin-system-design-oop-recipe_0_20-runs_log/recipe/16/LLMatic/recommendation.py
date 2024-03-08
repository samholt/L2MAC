import random


class Recommendation:

	def __init__(self, user, recipes):
		self.user = user
		self.recipes = recipes

	def generate_recommendations(self):
		# Mocking user preferences and past activity with random choice
		recommended_recipes = random.choices(self.recipes, k=5)
		return recommended_recipes

	def notify_user(self, new_recipes):
		# Mocking notification with print statements
		for recipe in new_recipes:
			print(f'New recipe {recipe} might interest you!')

