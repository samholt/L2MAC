from dataclasses import dataclass


@dataclass
class User:
	id: int
	username: str
	password: str
	favorites: list
	submitted_recipes: list
	following: list

	def change_password(self, new_password):
		self.password = new_password

	def save_favorite(self, recipe_id):
		self.favorites.append(recipe_id)

	def follow(self, user_id):
		self.following.append(user_id)


@dataclass
class Admin(User):
	def edit_recipe(self, recipe_id, new_data):
		# Admin can edit any recipe
		pass

	def remove_recipe(self, recipe_id):
		# Admin can remove any recipe
		pass

	def get_site_statistics(self):
		# Admin can get site usage statistics
		pass


@dataclass
class Recipe:
	id: int
	title: str
	ingredients: list
	instructions: str
	image: str
	categories: list

	def edit(self, new_data):
		# Edit recipe details
		pass

	def delete(self):
		# Delete the recipe
		pass

	def is_valid(self):
		# Validate recipe format
		pass

	def has_valid_categories(self):
		# Validate recipe categories
		pass


@dataclass
class RecipeRating:
	recipe_id: int
	rating: int

	@staticmethod
	def submit_rating(recipe_id, rating):
		# Submit a new rating for a recipe
		pass

	@staticmethod
	def get_average_rating(recipe_id):
		# Get the average rating of a recipe
		pass


@dataclass
class RecipeReview:
	recipe_id: int
	review: str

	@staticmethod
	def submit_review(recipe_id, review):
		# Submit a new review for a recipe
		pass

	@staticmethod
	def get_reviews(recipe_id):
		# Get all reviews of a recipe
		pass


@dataclass
class RecipeSharing:
	recipe_id: int
	platform: str

	@staticmethod
	def share(recipe_id, platform):
		# Share a recipe on a social media platform
		pass
