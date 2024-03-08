import pytest
from user import User
from recipe import Recipe


def test_generate_recommendations():
	user = User('test_user', 'password')
	recipe1 = Recipe(['ingredient1'], 'instructions1', 'image1', 'category1', 'dietary_needs1', 'timestamp1')
	recipe2 = Recipe(['ingredient2'], 'instructions2', 'image2', 'category2', 'dietary_needs2', 'timestamp2')
	recipe3 = Recipe(['ingredient3'], 'instructions3', 'image3', 'category3', 'dietary_needs3', 'timestamp3')
	user.favorite_recipes.append(recipe1)
	user.submitted_recipes.append(recipe2)
	Recipe.recipe_db = {recipe1.instructions: recipe1, recipe2.instructions: recipe2, recipe3.instructions: recipe3}
	recommendations = user.generate_recommendations()
	assert len(recommendations) == 2
	assert recipe1 in recommendations
	assert recipe2 in recommendations
	assert recipe3 not in recommendations


def test_receive_notifications():
	user = User('test_user', 'password')
	recipe1 = Recipe(['ingredient1'], 'instructions1', 'image1', 'category1', 'dietary_needs1', 'timestamp1')
	recipe2 = Recipe(['ingredient2'], 'instructions2', 'image2', 'category2', 'dietary_needs2', 'timestamp2')
	recipe3 = Recipe(['ingredient3'], 'instructions3', 'image3', 'category3', 'dietary_needs3', 'timestamp3')
	user.favorite_recipes.append(recipe1)
	user.submitted_recipes.append(recipe2)
	user.feed.append(recipe1)
	user.feed.append(recipe2)
	Recipe.recipe_db = {recipe1.instructions: recipe1, recipe2.instructions: recipe2, recipe3.instructions: recipe3}
	new_recipes = user.receive_notifications()
	assert new_recipes == 'No new recipes'
