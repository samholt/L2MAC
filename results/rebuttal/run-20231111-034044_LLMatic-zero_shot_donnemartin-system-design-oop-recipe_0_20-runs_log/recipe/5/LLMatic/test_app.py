import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}


def test_get_user(client):
	response = client.get('/user/test')
	assert response.status_code == 200
	assert json.loads(response.data) == {'username': 'test', 'password': 'test'}


def test_create_recipe(client):
	response = client.post('/recipe', json={'name': 'test', 'ingredients': 'test', 'instructions': 'test', 'images': 'test', 'category': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Recipe created successfully'}


def test_get_recipe(client):
	response = client.get('/recipe/test')
	assert response.status_code == 200
	assert json.loads(response.data) == {'name': 'test', 'ingredients': 'test', 'instructions': 'test', 'images': 'test', 'category': 'test'}


def test_create_review(client):
	response = client.post('/review', json={'user': 'test', 'recipe': 'test', 'rating': 5, 'review_text': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Review created successfully'}


def test_get_review(client):
	response = client.get('/review/test')
	assert response.status_code == 200
	assert json.loads(response.data) == {'user': 'test', 'recipe': 'test', 'rating': 5, 'review_text': 'test'}


def test_create_admin(client):
	response = client.post('/admin', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Admin created successfully'}


def test_get_admin(client):
	response = client.get('/admin/test')
	assert response.status_code == 200
	assert json.loads(response.data) == {'username': 'test', 'password': 'test'}
