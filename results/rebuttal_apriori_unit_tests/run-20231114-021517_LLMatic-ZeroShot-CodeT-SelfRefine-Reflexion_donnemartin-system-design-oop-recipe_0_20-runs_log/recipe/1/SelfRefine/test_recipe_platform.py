import pytest
import random
import string

from recipe_platform.database import *


def test_recipe_submission():
	# Generate random data for recipe submission
	title = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
	ingredients = ['ingredient1', 'ingredient2']
	instructions = 'Mix and cook'
	image = 'image_url'
	categories = ['Italian', 'Gluten-Free']

	create_recipe(1, title, ingredients, instructions, image, categories)
	recipe = get_recipe_by_id(1)

	assert recipe.title == title
	assert recipe.ingredients == ingredients
	assert recipe.instructions == instructions
	assert recipe.image == image
	assert recipe.categories == categories


def test_recipe_edit_delete():
	new_title = 'New Title'
	edit_recipe(1, 1, {'title': new_title})
	recipe = get_recipe_by_id(1)
	assert recipe.title == new_title

	remove_recipe(1, 1)
	assert get_recipe_by_id(1) is None


def test_recipe_search():
	search_query = 'chocolate'
	create_recipe(2, search_query, [], '', '', [])
	search_result = search_recipes(search_query)
	assert all(search_query in recipe.title for recipe in search_result)


def test_recipe_categorization_search():
	category = 'Vegan'
	create_recipe(3, '', [], '', '', [category])
	search_result = search_recipes_by_category(category)
	assert all(category in recipe.categories for recipe in search_result)


def test_account_creation_management():
	user_data = {'id': 1, 'username': 'user123', 'password': 'pass123'}
	create_user(**user_data)
	user = get_user_by_username(user_data['username'])
	assert user.username == user_data['username']
	assert user.password == user_data['password']


def test_save_favorite_recipes():
	user_id = 1
	recipe_id = 2
	save_favorite(user_id, recipe_id)
	user = get_user_by_username('user123')
	assert recipe_id in user.favorites


def test_recipe_rating():
	recipe_id = 2
	rating = 5
	submit_rating(recipe_id, rating)
	average_rating = get_average_rating(recipe_id)
	assert average_rating == rating


def test_recipe_review():
	recipe_id = 2
	review = 'Great recipe!'
	submit_review(recipe_id, review)
	reviews = get_reviews(recipe_id)
	assert any(r.review == review for r in reviews)


def test_user_following():
	follower_id = 1
	followee_id = 2
	create_user(followee_id, 'user2', 'pass2')
	follow(follower_id, followee_id)
	follower = get_user_by_username('user123')
	assert followee_id in follower.following


def test_admin_manage_recipes():
	admin_data = {'id': 1, 'username': 'admin1', 'password': 'adminpass'}
	create_admin(**admin_data)
	admin = get_admin_by_username(admin_data['username'])
	assert admin.username == admin_data['username']
	assert admin.password == admin_data['password']

	recipe_id = 3
	new_data = {'title': 'Updated Title'}
	edit_recipe(admin.id, recipe_id, new_data)
	recipe = get_recipe_by_id(recipe_id)
	assert recipe.title == new_data['title']

	remove_recipe(admin.id, recipe_id)
	assert get_recipe_by_id(recipe_id) is None
