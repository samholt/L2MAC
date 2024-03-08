import pytest
import app
import json


def test_create_user():
	response = app.app.test_client().post('/users', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == 'User created successfully'


def test_get_users():
	response = app.app.test_client().get('/users')
	assert response.status_code == 200
	assert isinstance(response.get_json(), dict)


def test_submit_recipe():
	response = app.app.test_client().post('/recipes', data=json.dumps({'recipe_id': '1', 'name': 'test', 'ingredients': ['test']}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe submitted successfully'}


def test_get_recipes():
	response = app.app.test_client().get('/recipes')
	assert response.status_code == 200
	assert isinstance(response.get_json(), dict)


def test_submit_review():
	response = app.app.test_client().post('/reviews', data=json.dumps({'username': 'test', 'recipe': '1', 'rating': 5, 'review_text': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Review submitted successfully'


def test_get_reviews():
	response = app.app.test_client().get('/reviews')
	assert response.status_code == 200
	assert isinstance(response.get_json(), dict)


def test_create_category():
	response = app.app.test_client().post('/categories', data=json.dumps({'recipe_id': '1', 'name': 'test', 'ingredients': ['test'], 'categories': ['test']}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe categorized successfully'}


def test_get_categories():
	response = app.app.test_client().get('/categories')
	assert response.status_code == 200
	assert isinstance(response.get_json(), dict)


def test_manage_recipes():
	response = app.app.test_client().post('/admin', data=json.dumps({'recipe_id': '1', 'action': 'delete'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe not found'}


def test_get_admin():
	response = app.app.test_client().get('/admin')
	assert response.status_code == 200


def test_generate_recommendations():
	response = app.app.test_client().post('/recommendations', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Recommendations generated successfully'


def test_get_recommendations():
	response = app.app.test_client().get('/recommendations')
	assert response.status_code == 200
	assert isinstance(response.get_json(), dict)

