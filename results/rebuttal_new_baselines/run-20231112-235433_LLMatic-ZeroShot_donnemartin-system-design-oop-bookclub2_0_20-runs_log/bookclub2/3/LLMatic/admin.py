class Admin:
	admins = {}

	def __init__(self):
		self.dashboard = {}
		self.user_data = {}
		self.book_data = {}
		self.__class__.admins[self] = self

	def access_dashboard(self):
		return self.dashboard

	def moderate_content(self, content_id):
		if not content_id:
			raise ValueError('Missing required parameters')
		# Mock moderation
		return 'Content moderated'

	def manage_users(self, user_id, action):
		if not user_id or not action:
			raise ValueError('Missing required parameters')
		# Mock user management
		return 'User managed'

	def generate_analytics(self):
		# Mock analytics generation
		user_engagement = len(self.user_data)
		popular_books = sorted(self.book_data.items(), key=lambda x: x[1], reverse=True)
		return user_engagement, popular_books
