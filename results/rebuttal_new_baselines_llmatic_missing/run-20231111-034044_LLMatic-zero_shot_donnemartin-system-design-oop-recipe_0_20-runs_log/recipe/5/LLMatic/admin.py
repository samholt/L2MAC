from user import User
from recipe import Recipe


class Admin(User):
	def __init__(self, username, password):
		super().__init__(username, password)
		self.managed_recipes = {}

	def manage_recipe(self, recipe):
		if isinstance(recipe, Recipe):
			self.managed_recipes[recipe.name] = recipe
			return 'Recipe managed successfully'
		else:
			return 'Invalid recipe'

	def remove_recipe(self, recipe):
		if recipe.name in self.managed_recipes:
			del self.managed_recipes[recipe.name]
			return 'Recipe removed successfully'
		else:
			return 'Recipe not found'

	def monitor_site_usage(self):
		# Mocking site usage statistics
		return {'total_users': len(self.following), 'total_recipes': len(self.managed_recipes)}

	def monitor_user_engagement(self):
		# Mocking user engagement data
		return {'average_submitted_recipes': sum(len(user.submitted_recipes) for user in self.following) / len(self.following) if self.following else 0}
