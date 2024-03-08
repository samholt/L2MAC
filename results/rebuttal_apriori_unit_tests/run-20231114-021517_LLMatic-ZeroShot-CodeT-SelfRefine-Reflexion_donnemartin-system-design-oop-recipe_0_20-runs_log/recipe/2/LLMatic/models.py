class User:
	users = {}

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.favorites = []
		self.submitted_recipes = []
		User.users[username] = self

	@classmethod
	def get_by_username(cls, username):
		return cls.users.get(username)

	def change_password(self, new_password):
		self.password = new_password

	def save_favorite(self, recipe_id):
		self.favorites.append(recipe_id)

	def submit_recipe(self, recipe):
		self.submitted_recipes.append(recipe)


class Recipe:
	recipes = {}
	id_counter = 1

	def __init__(self, title, ingredients, instructions, image, categories, user, type=None, cuisine=None, dietary_needs=None):
		self.id = Recipe.id_counter
		Recipe.id_counter += 1
		self.title = title
		self.ingredients = ingredients
		self.instructions = instructions
		self.image = image
		self.categories = categories
		self.user = user
		self.type = type
		self.cuisine = cuisine
		self.dietary_needs = dietary_needs
		Recipe.recipes[self.id] = self

	@staticmethod
	def validate_data(data):
		return all(data.get(field) for field in ['title', 'ingredients', 'instructions', 'image', 'categories'])

	@classmethod
	def get_by_id(cls, id):
		return cls.recipes.get(id)

	def edit(self, data):
		for field in ['title', 'ingredients', 'instructions', 'image', 'categories']:
			if data.get(field):
				setattr(self, field, data[field])

	def delete(self):
		if self.id in Recipe.recipes:
			del Recipe.recipes[self.id]

	@classmethod
	def all(cls):
		return list(cls.recipes.values())


class Review:
	def __init__(self, text, user, recipe):
		self.text = text
		self.user = user
		self.recipe = recipe


class Rating:
	def __init__(self, stars, user, recipe):
		self.stars = stars
		self.user = user
		self.recipe = recipe

