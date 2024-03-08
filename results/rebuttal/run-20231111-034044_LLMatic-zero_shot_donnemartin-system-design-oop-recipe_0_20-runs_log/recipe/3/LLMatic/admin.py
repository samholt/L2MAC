from user import User

class Admin(User):
	def __init__(self, username, password):
		super().__init__(username, password)
		self.managed_recipes = []

	def manage_recipe(self, recipe):
		self.managed_recipes.append(recipe)

	def remove_inappropriate_content(self, content):
		if content in self.managed_recipes:
			self.managed_recipes.remove(content)
