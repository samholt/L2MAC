class RecipeSubmission:
	def __init__(self, title, ingredients, instructions, image, categories=[]):
		self.title = title
		self.ingredients = ingredients
		self.instructions = instructions
		self.image = image
		self.categories = categories

	def is_valid(self):
		return bool(self.title and self.ingredients and self.instructions and self.image)

	def has_valid_categories(self):
		valid_categories = ['Italian', 'Gluten-Free', 'Vegan', 'Vegetarian', 'Dessert', 'Main Course', 'Appetizer', 'Side Dish', 'Drink']
		return all(category in valid_categories for category in self.categories)

	@staticmethod
	def get_by_id(id):
		# Mock database lookup
		return None

	def edit(self, title=None, ingredients=None, instructions=None, image=None, categories=None):
		if title:
			self.title = title
		if ingredients:
			self.ingredients = ingredients
		if instructions:
			self.instructions = instructions
		if image:
			self.image = image
		if categories:
			self.categories = categories

	def delete(self):
		# Mock database delete
		pass

	@staticmethod
	def search(query):
		# Mock database search
		return []

	@staticmethod
	def search_by_category(category):
		# Mock database search
		return []


# User class

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.favorites = []
		self.submitted_recipes = []

	@staticmethod
	def create(username, password):
		# Mock database create
		return User(username, password)

	def change_password(self, new_password):
		self.password = new_password

	def save_favorite(self, recipe_id):
		self.favorites.append(recipe_id)

	@staticmethod
	def get_by_username(username):
		# Mock database lookup
		return User(username, 'password')

	def get_profile_page_content(self):
		# Mock database lookup
		return {'username': self.username, 'favorites': self.favorites, 'submitted_recipes': self.submitted_recipes}

	def is_valid(self):
		return bool(self.username and self.password)


# RecipeRating class

class RecipeRating:
	def __init__(self):
		self.ratings = {}

	def submit_rating(self, recipe_id, rating):
		if recipe_id not in self.ratings:
			self.ratings[recipe_id] = []
		self.ratings[recipe_id].append(rating)

	def get_average_rating(self, recipe_id):
		if recipe_id in self.ratings:
			return sum(self.ratings[recipe_id]) / len(self.ratings[recipe_id])
		return None


# RecipeReview class

class RecipeReview:
	def __init__(self):
		self.reviews = {}

	def submit_review(self, recipe_id, review):
		if recipe_id not in self.reviews:
			self.reviews[recipe_id] = []
		self.reviews[recipe_id].append(review)

	def get_reviews(self, recipe_id):
		return self.reviews.get(recipe_id, [])
