class Admin:
	def __init__(self):
		self.users = []
		self.recipes = []

	def add_user(self, user):
		self.users.append(user)

	def remove_user(self, user):
		self.users.remove(user)

	def add_recipe(self, recipe):
		self.recipes.append(recipe)

	def remove_recipe(self, recipe):
		self.recipes.remove(recipe)

	def get_site_statistics(self):
		return {
			'Number of Users': len(self.users),
			'Number of Recipes': len(self.recipes)
		}

	def get_user_engagement(self):
		engagement = {}
		for user in self.users:
			engagement[user.username] = len(user.submitted_recipes)
		return engagement
