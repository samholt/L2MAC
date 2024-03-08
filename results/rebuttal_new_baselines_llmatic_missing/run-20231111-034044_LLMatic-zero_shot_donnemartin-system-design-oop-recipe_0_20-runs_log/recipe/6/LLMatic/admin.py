class Admin:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.recipes = {}
		self.site_usage_stats = {}
		self.user_engagement = {}

	def manage_recipes(self, recipe_id, action):
		if action == 'remove':
			self.recipes.pop(recipe_id, None)
		elif action == 'add':
			self.recipes[recipe_id] = 'Added'
		return self.recipes

	def remove_inappropriate_content(self, content_id):
		# Assuming content_id is the key of the content in a dictionary
		self.recipes.pop(content_id, None)
		return self.recipes

	def monitor_site_usage(self, user_id, action):
		if user_id not in self.site_usage_stats:
			self.site_usage_stats[user_id] = {'views': 0, 'actions': 0}
		if action == 'view':
			self.site_usage_stats[user_id]['views'] += 1
		elif action == 'action':
			self.site_usage_stats[user_id]['actions'] += 1
		return self.site_usage_stats

	def monitor_user_engagement(self, user_id, engagement):
		if user_id not in self.user_engagement:
			self.user_engagement[user_id] = 0
		self.user_engagement[user_id] += engagement
		return self.user_engagement
