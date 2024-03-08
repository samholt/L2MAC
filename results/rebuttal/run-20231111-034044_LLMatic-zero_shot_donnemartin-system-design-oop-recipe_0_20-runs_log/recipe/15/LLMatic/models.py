from datetime import datetime
from typing import List


class User:
	def __init__(self, username: str, password: str, email: str, favorite_recipes: List[str], submitted_recipes: List[str] = []):
		self.username = username
		self.password = password
		self.email = email
		self.favorite_recipes = favorite_recipes
		self.submitted_recipes = submitted_recipes

	def to_json(self):
		return {
			'username': self.username,
			'email': self.email,
			'favorite_recipes': self.favorite_recipes,
			'submitted_recipes': self.submitted_recipes
		}


class Recipe:
	def __init__(self, name: str, ingredients: str, instructions: str, image: str, categories: List[str], submitted_by: str):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions
		self.image = image
		self.categories = categories
		self.submitted_by = submitted_by
		self.submission_date = datetime.now()

	def to_json(self):
		return {
			'name': self.name,
			'ingredients': self.ingredients,
			'instructions': self.instructions,
			'image': self.image,
			'categories': self.categories,
			'submitted_by': self.submitted_by,
			'submission_date': self.submission_date.strftime('%Y-%m-%d %H:%M:%S')
		}


class Review:
	def __init__(self, username: str, recipe_name: str, rating: int, comment: str):
		self.username = username
		self.recipe_name = recipe_name
		self.rating = rating
		self.comment = comment
		self.submission_date = datetime.now()

	def to_json(self):
		return {
			'username': self.username,
			'recipe_name': self.recipe_name,
			'rating': self.rating,
			'comment': self.comment,
			'submission_date': self.submission_date.strftime('%Y-%m-%d %H:%M:%S')
		}


class Follow:
	def __init__(self, follower: str, following: str):
		self.follower = follower
		self.following = following

	def to_json(self):
		return {
			'follower': self.follower,
			'following': self.following
		}

