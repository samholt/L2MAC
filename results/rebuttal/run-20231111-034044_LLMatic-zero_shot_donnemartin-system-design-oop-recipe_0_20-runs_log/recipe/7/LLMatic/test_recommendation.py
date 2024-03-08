import pytest

from recommendation import Recommendation
from user import User
from recipe import Recipe


def test_generate_recommendations():
	recommendation = Recommendation()

	# Add users
	user1 = User('John', 'password')
	user1.set_preferences(['Italian', 'Mexican'])
	recommendation.add_user(user1)

	# Add recipes
	recipe1 = Recipe('Pizza', 'Tomato, Cheese, Dough', 'Instructions', 'Image', 'Italian')
	recipe2 = Recipe('Tacos', 'Tortilla, Beef, Cheese', 'Instructions', 'Image', 'Mexican')
	recipe3 = Recipe('Sushi', 'Rice, Fish', 'Instructions', 'Image', 'Japanese')
	recommendation.add_recipe(recipe1)
	recommendation.add_recipe(recipe2)
	recommendation.add_recipe(recipe3)

	# Generate recommendations for user1
	recommended_recipes = recommendation.generate_recommendations('John')
	assert len(recommended_recipes) <= 10
	for recipe in recommended_recipes:
		assert recipe.category in user1.get_preferences()


def test_notify_user():
	recommendation = Recommendation()

	# Add users
	user1 = User('John', 'password')
	user1.set_preferences(['Italian', 'Mexican'])
	recommendation.add_user(user1)

	# Add recipes
	recipe1 = Recipe('Pizza', 'Tomato, Cheese, Dough', 'Instructions', 'Image', 'Italian')
	recipe2 = Recipe('Tacos', 'Tortilla, Beef, Cheese', 'Instructions', 'Image', 'Mexican')
	recipe3 = Recipe('Sushi', 'Rice, Fish', 'Instructions', 'Image', 'Japanese')
	recommendation.add_recipe(recipe1)
	recommendation.add_recipe(recipe2)
	recommendation.add_recipe(recipe3)

	# Notify user1
	assert recommendation.notify_user('John') == True
	assert recommendation.notify_user('Jane') == False
