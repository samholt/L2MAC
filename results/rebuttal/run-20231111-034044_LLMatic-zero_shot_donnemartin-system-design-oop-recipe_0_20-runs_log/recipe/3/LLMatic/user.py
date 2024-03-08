class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.followed_users = []
		self.preferences = []
		self.activity = []

	def create_account(self, username, password, preferences):
		self.username = username
		self.password = password
		self.preferences = preferences
		return {'message': 'Account created successfully', 'user': {'username': self.username, 'preferences': self.preferences}}

	def manage_account(self, username=None, password=None, preferences=None):
		if username:
			self.username = username
		if password:
			self.password = password
		if preferences:
			self.preferences = preferences

	def save_favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def follow_user(self, user):
		self.followed_users.append(user)

	def add_activity(self, action):
		self.activity.append(action)

	def get_recent_activity(self):
		return self.activity

	def get_following(self):
		return self.followed_users
