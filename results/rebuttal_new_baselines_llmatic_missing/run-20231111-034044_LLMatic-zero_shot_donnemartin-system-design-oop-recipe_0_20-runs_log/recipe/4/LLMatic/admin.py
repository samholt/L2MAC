class Admin:
	def __init__(self):
		self.recipes = {}
		self.users = {}

	def manage_recipes(self, recipe_id, action):
		if action == 'delete':
			if recipe_id in self.recipes:
				del self.recipes[recipe_id]
				return 'Recipe deleted'
			else:
				return 'Recipe not found'
		elif action == 'view':
			if recipe_id in self.recipes:
				return self.recipes[recipe_id]
			else:
				return 'Recipe not found'

	def remove_inappropriate_content(self, user_id):
		if user_id in self.users:
			user = self.users[user_id]
			user['content'] = [content for content in user['content'] if not content['inappropriate']]
			return 'Inappropriate content removed'
		else:
			return 'User not found'
