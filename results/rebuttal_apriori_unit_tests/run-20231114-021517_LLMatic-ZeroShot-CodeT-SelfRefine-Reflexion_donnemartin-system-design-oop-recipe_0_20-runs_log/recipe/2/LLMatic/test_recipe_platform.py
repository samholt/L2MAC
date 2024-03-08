import pytest
import random
import string

from models import Recipe, User

def test_account_creation_management():
	user_data = {'username': 'user123', 'password': 'pass123'}
	user = User(**user_data)
	assert user.username == user_data['username']
	assert user.password == user_data['password']

	new_password = 'newpass123'
	user.change_password(new_password)
	assert user.password == new_password

def test_save_favorite_recipes():
	user = User('user123', 'pass123')
	recipe_id = random.randint(1, 1000)
	user.save_favorite(recipe_id)
	assert recipe_id in user.favorites

def test_profile_page_content():
	user = User('user123', 'pass123')
	assert hasattr(user, 'submitted_recipes')
	assert hasattr(user, 'favorites')

def test_recipe_submission():
	title = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
	ingredients = ['ingredient1', 'ingredient2']
	instructions = 'Mix and cook'
	image = 'image_url'
	categories = ['Italian', 'Gluten-Free']
	user = User('user123', 'pass123')

	recipe = Recipe(title, ingredients, instructions, image, categories, user)
	user.submit_recipe(recipe)
	assert recipe in user.submitted_recipes

def test_recipe_categorization():
	categories = ['Italian', 'Gluten-Free']
	user = User('user123', 'pass123')
	recipe = Recipe('Pizza', ['ingredient1', 'ingredient2'], 'Mix and cook', 'image_url', categories, user)
	assert categories == recipe.categories

def test_recipe_edit_delete():
	user = User('user123', 'pass123')
	recipe = Recipe('Pizza', ['ingredient1', 'ingredient2'], 'Mix and cook', 'image_url', ['Italian'], user)
	new_title = 'New Title'
	recipe.edit({'title': new_title})
	assert recipe.title == new_title

	recipe_id = recipe.id
	recipe.delete()
	assert Recipe.get_by_id(recipe_id) is None

