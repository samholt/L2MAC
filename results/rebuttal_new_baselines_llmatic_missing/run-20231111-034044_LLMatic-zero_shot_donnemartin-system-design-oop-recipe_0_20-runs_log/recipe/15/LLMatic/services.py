from models import User, Recipe, Review, Follow

class UserService:
	def __init__(self):
		self.users = {}

	def create_user(self, username, password, email, favorite_recipes):
		user = User(username, password, email, favorite_recipes)
		self.users[username] = user
		return user

	def get_user(self, username):
		return self.users.get(username)

	def update_user(self, username, password, email, favorite_recipes):
		user = self.users.get(username)
		if user:
			user.password = password
			user.email = email
			user.favorite_recipes = favorite_recipes
		return user

	def save_favorite_recipe(self, username, recipe_name):
		user = self.users.get(username)
		if user:
			user.favorite_recipes.append(recipe_name)
		return user

	def get_user_count(self):
		return len(self.users)

	def get_user_submitted_recipes(self, username):
		user = self.users.get(username)
		if user:
			return user.submitted_recipes
		return None

class RecipeService:
	def __init__(self):
		self.recipes = {}

	def create_recipe(self, name, ingredients, instructions, image, categories, submitted_by):
		recipe = Recipe(name, ingredients, instructions, image, categories, submitted_by)
		self.recipes[name] = recipe
		return recipe

	def update_recipe(self, name, ingredients, instructions, image, categories, submitted_by):
		recipe = self.recipes.get(name)
		if recipe:
			recipe.ingredients = ingredients
			recipe.instructions = instructions
			recipe.image = image
			recipe.categories = categories
			recipe.submitted_by = submitted_by
		return recipe

	def get_recipe(self, name):
		return self.recipes.get(name)

	def delete_recipe(self, name):
		return self.recipes.pop(name, None)

	def get_all_recipes(self):
		return list(self.recipes.values())

	def get_recipe_count(self):
		return len(self.recipes)

	def get_recipe_recommendations(self, user):
		return [recipe for recipe in self.recipes.values() if any(category in user.favorite_recipes for category in recipe.categories)]

