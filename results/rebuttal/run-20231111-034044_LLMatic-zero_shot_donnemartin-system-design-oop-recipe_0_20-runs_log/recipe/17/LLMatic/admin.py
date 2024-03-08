class Admin:
	def __init__(self):
		self.users = {}
		self.recipes = {}

	def add_user(self, user):
		self.users[user.username] = user

	def remove_user(self, username):
		if username in self.users:
			del self.users[username]

	def add_recipe(self, recipe):
		self.recipes[recipe.name] = recipe

	def remove_recipe(self, recipe_name):
		if recipe_name in self.recipes:
			del self.recipes[recipe_name]

	def get_site_statistics(self):
		return {
			'number_of_users': len(self.users),
			'number_of_recipes': len(self.recipes)
		}
