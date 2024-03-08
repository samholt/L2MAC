from models import User, Recipe

users = {}
recipes = {}

def create_user(id: int, name: str) -> User:
	user = User(id, name)
	users[id] = user
	return user

def create_recipe(id: int, name: str, ingredients: list, instructions: list, image: str, categories: list) -> Recipe:
	recipe = Recipe(id, name, ingredients, instructions, image, categories)
	recipes[id] = recipe
	return recipe

def add_favorite(user_id: int, recipe_id: int) -> None:
	users[user_id].favorites.append(recipe_id)
