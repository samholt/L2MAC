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
		if recipe_id not in self.favorites:
			self.favorites.append(recipe_id)

	def follow(self, user_id):
		if user_id not in self.following:
			self.following.append(user_id)


@dataclass
class Admin(User):
	def edit_recipe(self, recipe_id, new_data):
		# Here we should update the recipe with the new data
		pass

	def remove_recipe(self, recipe_id):
		# Here we should remove the recipe from the database
		pass

	def get_site_statistics(self):
		# Here we should return the site usage statistics
		pass


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
		# Here we should check if the categories are valid
		pass


@dataclass
class RecipeRating:
	recipe_id: int
	rating: int

	@staticmethod
	def submit_rating(recipe_id, rating):
		# Here we should submit a new rating for the recipe
		pass

	@staticmethod
	def get_average_rating(recipe_id):
		# Here we should return the average rating of the recipe
		pass


@dataclass
class RecipeReview:
	recipe_id: int
	review: str

	@staticmethod
	def submit_review(recipe_id, review):
		# Here we should submit a new review for the recipe
		pass

	@staticmethod
	def get_reviews(recipe_id):
		# Here we should return all reviews of the recipe
		pass


@dataclass
class RecipeSharing:
	recipe_id: int
	platform: str

	@staticmethod
	def share(recipe_id, platform):
		# Here we should share the recipe on the specified platform
		pass
