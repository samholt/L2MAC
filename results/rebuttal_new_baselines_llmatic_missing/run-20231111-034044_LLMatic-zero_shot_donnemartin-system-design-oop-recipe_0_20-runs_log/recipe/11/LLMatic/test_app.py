import pytest
from app import app, user_manager, recipe_manager, review_manager, category_manager, recommendation_manager
from users import User
from recipes import RecipeManager
from reviews import Review
from categories import Category
from database import MockDatabase

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def mock_db():
	return MockDatabase()

@pytest.fixture
def user():
	return User('1', 'Test User', 'test@example.com')

@pytest.fixture
def recipe():
	return {'recipe_id': '1', 'user_id': '1', 'title': 'Test Recipe', 'description': 'Test Description', 'ingredients': 'Test Ingredients', 'category': 'Test Category'}

@pytest.fixture
def review():
	return {'user_id': '1', 'recipe_id': '1', 'rating': 5, 'review': 'Test Review'}

@pytest.fixture
def category():
	return {'category_name': 'Test Category', 'recipe_id': '1'}

# Add more tests here

# Test creating a user

def test_create_user(client, mock_db, user):
	mock_db.add_user(user)
	response = client.post('/users', json=user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == user.__dict__

# Test getting a user

def test_get_user(client, mock_db, user):
	mock_db.add_user(user)
	response = client.get(f'/users/{user.id}')
	assert response.status_code == 200
	assert response.get_json() == user.__dict__

# Test deleting a user

def test_delete_user(client, mock_db, user):
	mock_db.add_user(user)
	response = client.delete(f'/users/{user.id}')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User deleted successfully'}

# Test submitting a recipe

def test_submit_recipe(client, mock_db, recipe):
	mock_db.add_recipe(recipe)
	response = client.post('/recipes', json=recipe)
	assert response.status_code == 201
	assert response.get_json() == recipe

# Test getting a recipe

def test_get_recipe(client, mock_db, recipe):
	mock_db.add_recipe(recipe)
	response = client.get(f'/recipes/{recipe["recipe_id"]}')
	assert response.status_code == 200
	assert response.get_json() == recipe

# Test editing a recipe

def test_edit_recipe(client, mock_db, recipe):
	mock_db.add_recipe(recipe)
	response = client.put(f'/recipes/{recipe["recipe_id"]}', json={'title': 'New Title'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe edited successfully'}

# Test deleting a recipe

def test_delete_recipe(client, mock_db, recipe):
	mock_db.add_recipe(recipe)
	response = client.delete(f'/recipes/{recipe["recipe_id"]}')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe deleted successfully'}

# Test adding a review

def test_add_review(client, mock_db, review):
	mock_db.add_review(review)
	response = client.post('/reviews', json=review)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Review added successfully', 'status': 'success'}

# Test getting reviews

def test_get_reviews(client, mock_db, review):
	mock_db.add_review(review)
	response = client.get(f'/reviews/{review["recipe_id"]}')
	assert response.status_code == 200
	assert response.get_json() == {'data': [{'rating': review['rating'], 'review': review['review'], 'user_id': review['user_id']}], 'status': 'success'}

# Test adding a category

def test_add_category(client, mock_db, category):
	mock_db.add_category(category)
	response = client.post('/categories', json=category)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Category added successfully'}

# Test getting recipes by category

def test_get_recipes_by_category(client, mock_db, category):
	mock_db.add_category(category)
	response = client.get(f'/categories/{category["category_name"]}')
	assert response.status_code == 200
	assert response.get_json() == [category['recipe_id']]

# Test getting all recipes

def test_get_all_recipes(client, mock_db):
	recipe = {'recipe_id': '1', 'user_id': '1', 'title': 'Test Recipe', 'description': 'Test Description', 'ingredients': 'Test Ingredients', 'category': 'Test Category'}
	mock_db.add_recipe(recipe)
	response = client.get('/admin/recipes')
	assert response.status_code == 200
	assert response.get_json() == [recipe]

# Test deleting a recipe as admin

def test_delete_recipe_admin(client, mock_db):
	recipe = {'recipe_id': '1', 'user_id': '1', 'title': 'Test Recipe', 'description': 'Test Description', 'ingredients': 'Test Ingredients', 'category': 'Test Category'}
	mock_db.add_recipe(recipe)
	response = client.delete(f'/admin/recipes/{recipe["recipe_id"]}')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe deleted successfully'}

# Test getting recommendations

def test_get_recommendations(client, mock_db, user):
	mock_db.add_user(user)
	response = client.get(f'/recommendations/{user.id}')
	assert response.status_code == 200
	assert response.get_json() == []

