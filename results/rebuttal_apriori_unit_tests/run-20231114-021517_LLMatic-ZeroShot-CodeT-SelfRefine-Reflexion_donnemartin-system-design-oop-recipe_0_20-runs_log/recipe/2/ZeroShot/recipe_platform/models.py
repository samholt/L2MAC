from dataclasses import dataclass


@dataclass
class User:
	id: int
	username: str
	password: str
	favorites: list
	following: list
	submitted_recipes: list

	def change_password(self, new_password):
		self.password = new_password

	def save_favorite(self, recipe_id):
		self.favorites.append(recipe_id)

	def follow(self, user_id):
		self.following.append(user_id)


@dataclass
class Admin(User):
	def edit_recipe(self, recipe_id, new_data):
		# This is a placeholder. In a real system, this would interact with a database.
		pass

	def remove_recipe(self, recipe_id):
		# This is a placeholder. In a real system, this would interact with a database.
		pass

	def get_site_statistics(self):
		# This is a placeholder. In a real system, this would interact with a database.
		return {'total_users': 0, 'total_recipes': 0}


@dataclass
class Recipe:
	id: int
	title: str
	ingredients: list
	instructions: str
	image: str
	categories: list

	def is_valid(self):
		return bool(self.title and self.ingredients and self.instructions and self.image)

	def has_valid_categories(self):
		# This is a placeholder. In a real system, this would interact with a database.
		return True


@dataclass
class RecipeRating:
	recipe_id: int
	rating: int

	@staticmethod
	def get_average_rating(recipe_id):
		# This is a placeholder. In a real system, this would interact with a database.
		return 5.0


@dataclass
class RecipeReview:
	recipe_id: int
	review: str

	@staticmethod
	def get_reviews(recipe_id):
		# This is a placeholder. In a real system, this would interact with a database.
		return []


@dataclass
class RecipeSharing:
	recipe_id: int
	platform: str

	@staticmethod
	def share(recipe_id, platform):
		# This is a placeholder. In a real system, this would interact with a database.
		return True
