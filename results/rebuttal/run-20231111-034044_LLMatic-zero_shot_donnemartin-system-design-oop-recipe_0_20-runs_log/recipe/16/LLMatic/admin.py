from user import User
from recipe import Recipe

class Admin(User):
	def __init__(self, username, password):
		super().__init__(username, password)

	def manage_recipes(self, recipe, action):
		if action == 'delete':
			self.submitted_recipes.remove(recipe)
			recipe.delete_recipe(self.submitted_recipes)
		elif action == 'edit':
			# Edit recipe
			pass

	def remove_inappropriate_content(self, content):
		# Remove inappropriate content
			pass
