class Admin:
	def __init__(self):
		self.recipes = {}
		self.users = {}
		self.site_usage = {'total_visits': 0, 'total_time_spent': 0, 'total_recipes_submitted': 0}

	def manage_recipes(self, recipe_id, action):
		if action == 'remove':
			if recipe_id in self.recipes:
				del self.recipes[recipe_id]
				return 'Recipe removed successfully'
			else:
				return 'Recipe not found'
		elif action == 'view':
			if recipe_id in self.recipes:
				return self.recipes[recipe_id]
			else:
				return 'Recipe not found'

	def manage_users(self, user_id, action):
		if action == 'remove':
			if user_id in self.users:
				del self.users[user_id]
				return 'User removed successfully'
			else:
				return 'User not found'
		elif action == 'view':
			if user_id in self.users:
				return self.users[user_id]
			else:
				return 'User not found'

	def monitor_site_usage(self):
		return self.site_usage
