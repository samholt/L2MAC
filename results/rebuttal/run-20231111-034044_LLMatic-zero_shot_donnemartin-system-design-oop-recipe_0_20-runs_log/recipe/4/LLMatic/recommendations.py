import random

# Mock database
user_preferences = {}
user_activity = {}
recipes = {}


def set_user_preferences(user_id, preferences):
	user_preferences[user_id] = preferences


def get_user_preferences(user_id):
	return user_preferences.get(user_id, [])


def add_user_activity(user_id, recipe_id):
	if user_id not in user_activity:
		user_activity[user_id] = []
	user_activity[user_id].append(recipe_id)


def get_user_activity(user_id):
	return user_activity.get(user_id, [])


def generate_recommendations(user_id, num_recommendations=5):
	user_pref = get_user_preferences(user_id)
	user_act = get_user_activity(user_id)

	# Filter out recipes that the user has already interacted with
	potential_recipes = [recipe for recipe in recipes.keys() if recipe not in user_act]

	# Prioritize recipes that match the user's preferences
	priority_recipes = [recipe for recipe in potential_recipes if any(pref in recipes[recipe]['categories'] for pref in user_pref)]

	# If there are not enough priority recipes, fill in with other recipes
	if len(priority_recipes) < num_recommendations:
		filler_recipes = list(set(potential_recipes) - set(priority_recipes))
		if len(filler_recipes) < num_recommendations - len(priority_recipes):
			filler_recipes.extend(filler_recipes)
		priority_recipes.extend(filler_recipes[:num_recommendations - len(priority_recipes)])

	# If there are still not enough recipes, return all available recipes
	if len(priority_recipes) < num_recommendations:
		return priority_recipes

	return random.sample(priority_recipes, num_recommendations)
