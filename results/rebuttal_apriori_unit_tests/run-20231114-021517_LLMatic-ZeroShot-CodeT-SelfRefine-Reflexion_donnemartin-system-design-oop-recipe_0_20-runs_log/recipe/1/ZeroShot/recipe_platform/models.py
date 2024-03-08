from dataclasses import dataclass

# Mock database
DB = {}

@dataclass
class User:
	id: int
	username: str
	password: str
	favorites: list = []
	following: list = []
	interests: list = []

	@classmethod
	def create(cls, username, password):
		id = len(DB.get('users', [])) + 1
		user = cls(id, username, password)
		DB.setdefault('users', []).append(user)
		return user

	@classmethod
	def get_by_username(cls, username):
		for user in DB.get('users', []):
			if user.username == username:
				return user

	def change_password(self, new_password):
		self.password = new_password

	def save_favorite(self, recipe_id):
		self.favorites.append(recipe_id)

	def follow(self, user_id):
		self.following.append(user_id)

	def add_interest(self, interest):
		self.interests.append(interest)

	def get_notifications(self):
		# Mock implementation
		return ['new_{}_recipe'.format(interest) for interest in self.interests]

@dataclass
class Recipe:
	id: int
	title: str
	ingredients: list
	instructions: str
	image: str
	categories: list = []

	@classmethod
	def create(cls, title, ingredients, instructions, image, categories=[]):
		id = len(DB.get('recipes', [])) + 1
		recipe = cls(id, title, ingredients, instructions, image, categories)
		DB.setdefault('recipes', []).append(recipe)
		return recipe

	@classmethod
	def get_by_id(cls, id):
		for recipe in DB.get('recipes', []):
			if recipe.id == id:
				return recipe

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
		DB['recipes'].remove(self)

	@classmethod
	def search(cls, query):
		return [recipe for recipe in DB.get('recipes', []) if query in recipe.title]

	@classmethod
	def search_by_category(cls, category):
		return [recipe for recipe in DB.get('recipes', []) if category in recipe.categories]

@dataclass
class Rating:
	recipe_id: int
	rating: int

	@classmethod
	def submit_rating(cls, recipe_id, rating):
		DB.setdefault('ratings', []).append(cls(recipe_id, rating))

	@classmethod
	def get_average_rating(cls, recipe_id):
		recipe_ratings = [rating.rating for rating in DB.get('ratings', []) if rating.recipe_id == recipe_id]
		return sum(recipe_ratings) / len(recipe_ratings) if recipe_ratings else 0

@dataclass
class Review:
	recipe_id: int
	text: str

	@classmethod
	def submit_review(cls, recipe_id, text):
		DB.setdefault('reviews', []).append(cls(recipe_id, text))

	@classmethod
	def get_reviews(cls, recipe_id):
		return [review for review in DB.get('reviews', []) if review.recipe_id == recipe_id]

@dataclass
class Admin(User):
	def edit_recipe(self, recipe_id, new_data):
		recipe = Recipe.get_by_id(recipe_id)
		if recipe:
			recipe.edit(**new_data)

	def remove_recipe(self, recipe_id):
		recipe = Recipe.get_by_id(recipe_id)
		if recipe:
			recipe.delete()

	def get_site_statistics(self):
		# Mock implementation
		return {
			'total_users': len(DB.get('users', [])),
			'total_recipes': len(DB.get('recipes', []))
		}
