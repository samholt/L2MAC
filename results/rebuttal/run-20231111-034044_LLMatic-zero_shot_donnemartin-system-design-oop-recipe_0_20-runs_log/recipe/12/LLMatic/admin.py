class Admin:
	def __init__(self):
		self.database = {}

	def manage_recipes(self, recipe_id, action):
		if action == 'delete':
			if recipe_id in self.database['recipes']:
				del self.database['recipes'][recipe_id]
				return 'Recipe deleted successfully'
			else:
				return 'Recipe not found'
		elif action == 'view':
			if recipe_id in self.database['recipes']:
				return self.database['recipes'][recipe_id]
			else:
				return 'Recipe not found'

	def remove_inappropriate_content(self, content_id):
		if content_id in self.database['content']:
			del self.database['content'][content_id]
			return 'Content removed successfully'
		else:
			return 'Content not found'

	def monitor_site_usage(self):
		return len(self.database['users']), len(self.database['recipes'])

	def monitor_user_engagement(self):
		user_engagement = {}
		for user in self.database['users']:
			user_engagement[user] = len(self.database['users'][user]['followed'])
		return user_engagement
