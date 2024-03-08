class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.submitted_recipes = []
		self.favorite_recipes = []
		self.followed_users = []
		self.activities = []
		self.preferences = []

	@classmethod
	def register(cls, data):
		username = data['username']
		password = data['password']
		return cls(username, password)

	@classmethod
	def login(cls, data):
		username = data['username']
		password = data['password']
		# Here should be the logic to validate the user credentials
		return cls(username, password)

	def create_account(self, username, password):
		self.username = username
		self.password = password

	def manage_account(self, username, password):
		self.username = username
		self.password = password

	def save_favorite_recipe(self, recipe):
		self.favorite_recipes.append(recipe)

	def follow_user(self, user):
		self.followed_users.append(user)

	def add_activity(self, activity):
		self.activities.append(activity)

	def get_following(self):
		return self.followed_users

	def get_recent_activity(self):
		return self.activities

	def set_preferences(self, preferences):
		self.preferences = preferences

	def get_preferences(self):
		return self.preferences

	def to_dict(self):
		return {
			'username': self.username,
			'password': self.password,
			'submitted_recipes': self.submitted_recipes,
			'favorite_recipes': self.favorite_recipes,
			'followed_users': self.followed_users,
			'activities': self.activities,
			'preferences': self.preferences
		}
