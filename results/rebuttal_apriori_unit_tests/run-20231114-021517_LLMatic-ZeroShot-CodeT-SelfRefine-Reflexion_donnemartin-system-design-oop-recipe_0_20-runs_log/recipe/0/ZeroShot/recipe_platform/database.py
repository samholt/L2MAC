from .models import User, Admin, Recipe, RecipeRating, RecipeReview, RecipeSharing


# Mock database
users = {}
admins = {}
recipes = {}
recipe_ratings = {}
recipe_reviews = {}
recipe_shares = {}


def get_user_by_username(username):
	return users.get(username)


def get_admin_by_username(username):
	return admins.get(username)


def get_recipe_by_id(recipe_id):
	return recipes.get(recipe_id)


def get_recipe_ratings_by_id(recipe_id):
	return recipe_ratings.get(recipe_id)


def get_recipe_reviews_by_id(recipe_id):
	return recipe_reviews.get(recipe_id)


def get_recipe_shares_by_id(recipe_id):
	return recipe_shares.get(recipe_id)
