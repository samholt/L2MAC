import pytest
import app
from users import create_user, get_user, delete_user
from recipes import Recipe
from reviews import Review
from categories import Categories
from admin import Admin
from recommendations import Recommendations


def test_create_user_route():
	with app.app.test_client() as c:
		response = c.post('/user', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 201
		assert get_user('test') is not None


def test_get_user_route():
	create_user('test', 'test')
	with app.app.test_client() as c:
		response = c.get('/user/test')
		assert response.status_code == 200
		assert response.get_json() == 'test'


def test_delete_user_route():
	create_user('test', 'test')
	with app.app.test_client() as c:
		response = c.delete('/user/test')
		assert response.status_code == 200
		assert get_user('test') is None


def test_submit_recipe_route():
	with app.app.test_client() as c:
		response = c.post('/recipe', json={'recipe_id': '1', 'recipe_data': {'name': 'test', 'ingredients': ['test']}})
		assert response.status_code == 201
		assert app.recipe.get_recipe('1') is not None


def test_get_recipe_route():
	app.recipe.submit_recipe('1', {'name': 'test', 'ingredients': ['test']})
	with app.app.test_client() as c:
		response = c.get('/recipe/1')
		assert response.status_code == 200
		assert response.get_json() == {'name': 'test', 'ingredients': ['test']}


def test_add_review_route():
	with app.app.test_client() as c:
		response = c.post('/review', json={'user_id': '1', 'recipe_id': '1', 'rating': 5, 'review': 'test'})
		assert response.status_code == 201
		assert app.review.reviews['1'] is not None


def test_get_recommendations_route():
	create_user('test', 'test')
	app.recommendations.generate_recommendations('test')
	with app.app.test_client() as c:
		response = c.get('/recommendations/test')
		assert response.status_code == 200
		assert response.get_json() == app.recommendations.get_recommendations('test')
