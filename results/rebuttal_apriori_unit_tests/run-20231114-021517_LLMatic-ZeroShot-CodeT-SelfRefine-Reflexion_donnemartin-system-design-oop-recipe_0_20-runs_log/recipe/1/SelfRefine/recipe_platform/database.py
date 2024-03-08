from .models import User, Admin, Recipe, Rating, Review, Activity


# Mock database
users = {}
admins = {}
recipes = {}
ratings = {}
reviews = {}
activities = {}


# User related operations

def create_user(id, username, password):
	users[id] = User(id, username, password, [], [], [])


def get_user_by_username(username):
	for user in users.values():
		if user.username == username:
			return user


def save_favorite(user_id, recipe_id):
	users[user_id].favorites.append(recipe_id)


def follow(user_id, followee_id):
	users[user_id].following.append(followee_id)


# Admin related operations

def create_admin(id, username, password):
	admins[id] = Admin(id, username, password, [], [], [])


def get_admin_by_username(username):
	for admin in admins.values():
		if admin.username == username:
			return admin


def edit_recipe(admin_id, recipe_id, new_data):
	recipe = recipes[recipe_id]
	for key, value in new_data.items():
		setattr(recipe, key, value)


def remove_recipe(admin_id, recipe_id):
	if recipe_id in recipes:
		del recipes[recipe_id]


# Recipe related operations

def create_recipe(id, title, ingredients, instructions, image, categories):
	recipes[id] = Recipe(id, title, ingredients, instructions, image, categories)


def get_recipe_by_id(id):
	return recipes.get(id)


def search_recipes(query):
	return [recipe for recipe in recipes.values() if query in recipe.title]


def search_recipes_by_category(category):
	return [recipe for recipe in recipes.values() if category in recipe.categories]


# Rating related operations

def submit_rating(recipe_id, rating):
	ratings[recipe_id] = ratings.get(recipe_id, []) + [Rating(recipe_id, rating)]


def get_average_rating(recipe_id):
	recipe_ratings = ratings.get(recipe_id, [])
	return sum(rating.rating for rating in recipe_ratings) / len(recipe_ratings) if recipe_ratings else 0


# Review related operations

def submit_review(recipe_id, review):
	reviews[recipe_id] = reviews.get(recipe_id, []) + [Review(recipe_id, review)]


def get_reviews(recipe_id):
	return reviews.get(recipe_id, [])


# Activity related operations

def add_activity(user_id, activity_type, activity_data):
	activities[user_id] = activities.get(user_id, []) + [Activity(user_id, activity_type, activity_data)]


def get_activities(user_id):
	return activities.get(user_id, [])
