class Admin:
	def __init__(self, username):
		self.username = username
		self.managed_recipes = []
		self.removed_contents = []
		self.site_usage_statistics = {}
		self.user_engagement = {}

	def manage_recipe(self, recipe):
		self.managed_recipes.append(recipe)
		return 'Manage recipe'

	def remove_content(self, content):
		self.removed_contents.append(content)
		return 'Remove content'

	def monitor_site_usage(self, usage_statistics):
		self.site_usage_statistics = usage_statistics
		return 'Monitor site usage'

	def monitor_user_engagement(self, user_engagement):
		self.user_engagement = user_engagement
		return 'Monitor user engagement'
