from dataclasses import dataclass

# Mock database
DB = {
	'users': {},
	'recipes': {},
	'ratings': {},
	'reviews': {},
	'admins': {}
}

@dataclass
class User:
	id: int
	username: str
	password: str
	favorites: list = []
	submitted_recipes: list = []
	following: list = []

	@classmethod
	def create(cls, **kwargs):
		user = cls(**kwargs)
		DB['users'][user.id] = user
		return user

	def change_password(self, new_password):
		self.password = new_password

	def save_favorite(self, recipe_id):
		self.favorites.append(recipe_id)

	def follow(self, user_id):
		self.following.append(user_id)

@dataclass
class Recipe:
	id: int
	title: str
	ingredients: list
	instructions: str
	image: str
	categories: list = []

	@classmethod
	def create(cls, **kwargs):
		recipe = cls(**kwargs)
		DB['recipes'][recipe.id] = recipe
		return recipe

	def edit(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

	def delete(self):
		DB['recipes'].pop(self.id, None)

@dataclass
class Rating:
	id: int
	recipe_id: int
	rating: int

	@classmethod
	def create(cls, **kwargs):
		rating = cls(**kwargs)
		DB['ratings'][rating.id] = rating
		return rating

@dataclass
class Review:
	id: int
	recipe_id: int
	review: str

	@classmethod
	def create(cls, **kwargs):
		review = cls(**kwargs)
		DB['reviews'][review.id] = review
		return review

@dataclass
class Admin:
	id: int
	username: str
	password: str

	@classmethod
	def create(cls, **kwargs):
		admin = cls(**kwargs)
		DB['admins'][admin.id] = admin
		return admin

	def edit_recipe(self, recipe_id, new_data):
		recipe = DB['recipes'].get(recipe_id)
		if recipe:
			recipe.edit(**new_data)

	def remove_recipe(self, recipe_id):
		recipe = DB['recipes'].get(recipe_id)
		if recipe:
			recipe.delete()

