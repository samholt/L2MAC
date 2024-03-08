class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.favorites = []
		self.submitted_recipes = []
		self.following = []
		self.activities = []

	def create_account(self):
		# Code to create account
		return True

	def login(self, password):
		# Code to authenticate user
		return self.password == password

	def logout(self):
		# Code to clear user session
		return True

	def change_password(self, old_password, new_password):
		# Code to change password
		if self.password == old_password:
			self.password = new_password
			return True
		return False

	def view_profile(self):
		# Code to return user's submitted recipes and favorite recipes
		return {'submitted_recipes': self.submitted_recipes, 'favorites': self.favorites}

	def save_favorite(self, recipe):
		self.favorites.append(recipe)

	@staticmethod
	def get_by_username(username):
		# Code to get user by username
		return User(username, 'password')

	def submit_recipe(self, recipe):
		self.submitted_recipes.append(recipe)
		self.activities.append({'type': 'new_recipe', 'recipe': recipe})

	def follow(self, user_id):
		self.following.append(user_id)

	def get_feed(self):
		# Code to get recent activities of followed users
		return {'recent_activity': self.activities}

	# Rest of the classes remain the same

class Review:
	def __init__(self, recipe_id, user, text):
		self.recipe_id = recipe_id
		self.user = user
		self.text = text

	def submit_review(self):
		# Code to submit review
		return True

	@staticmethod
	def get_reviews(recipe_id):
		# Code to get reviews by recipe_id
		return [Review(recipe_id, User('testuser', 'password'), 'Great recipe!')]

class Rating:
	def __init__(self, recipe_id, user, score):
		self.recipe_id = recipe_id
		self.user = user
		self.score = score

	def submit_rating(self):
		# Code to submit rating
		return True

	@staticmethod
	def get_average_rating(recipe_id):
		# Code to get average rating by recipe_id
		return 5

class Admin(User):
	def __init__(self, username, password):
		super().__init__(username, password)

	def manage_recipe(self, recipe_id, new_data):
		# Code to update recipe with new data
		return True

	def monitor_site_usage(self):
		# Code to return site usage statistics
		return {'total_users': 100, 'total_recipes': 200}
