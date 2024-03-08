class Admin:
	def __init__(self):
		self.database = {}

	def manage_recipes(self, recipe_id, action):
		if action == 'delete':
			if recipe_id in self.database:
				del self.database[recipe_id]
				return 'Recipe deleted'
			else:
				return 'Recipe not found'
		elif action == 'view':
			if recipe_id in self.database:
				return self.database[recipe_id]
			else:
				return 'Recipe not found'

	def remove_inappropriate_content(self, content_id):
		if content_id in self.database:
			del self.database[content_id]
			return 'Content removed'
		else:
			return 'Content not found'
