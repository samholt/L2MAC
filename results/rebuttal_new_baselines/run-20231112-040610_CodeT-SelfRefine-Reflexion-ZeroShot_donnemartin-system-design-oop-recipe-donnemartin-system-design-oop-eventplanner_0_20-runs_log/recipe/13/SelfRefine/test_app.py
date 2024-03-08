import pytest
import app
from app import User, Recipe, Review, Category

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return User(id='1', name='Test User', recipes=[], favorites=[], followers=[])

@pytest.fixture
def recipe():
	return Recipe(id='1', name='Test Recipe', ingredients=[], instructions=[], images=[], categories=[], user_id='1')

@pytest.fixture
def review():
	return Review(id='1', user_id='1', recipe_id='1', rating=5, comment='Great recipe!')

@pytest.fixture
def category():
	return Category(id='1', name='Test Category', recipes=[])


def test_create_user(client, user):
	response = client.post('/user', json=user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == user.__dict__


def test_handle_user(client, user):
	client.post('/user', json=user.__dict__)
	response = client.get('/user/1')
	assert response.status_code == 200
	assert response.get_json() == user.__dict__
	response = client.put('/user/1', json={'name': 'Updated User'})
	assert response.status_code == 200
	assert response.get_json()['name'] == 'Updated User'
	response = client.delete('/user/1')
	assert response.status_code == 204


def test_create_recipe(client, recipe):
	response = client.post('/recipe', json=recipe.__dict__)
	assert response.status_code == 201
	assert response.get_json() == recipe.__dict__


def test_handle_recipe(client, recipe):
	client.post('/recipe', json=recipe.__dict__)
	response = client.get('/recipe/1')
	assert response.status_code == 200
	assert response.get_json() == recipe.__dict__
	response = client.put('/recipe/1', json={'name': 'Updated Recipe'})
	assert response.status_code == 200
	assert response.get_json()['name'] == 'Updated Recipe'
	response = client.delete('/recipe/1')
	assert response.status_code == 204


def test_create_review(client, review):
	response = client.post('/review', json=review.__dict__)
	assert response.status_code == 201
	assert response.get_json() == review.__dict__


def test_handle_review(client, review):
	client.post('/review', json=review.__dict__)
	response = client.get('/review/1')
	assert response.status_code == 200
	assert response.get_json() == review.__dict__
	response = client.put('/review/1', json={'comment': 'Updated comment'})
	assert response.status_code == 200
	assert response.get_json()['comment'] == 'Updated comment'
	response = client.delete('/review/1')
	assert response.status_code == 204


def test_create_category(client, category):
	response = client.post('/category', json=category.__dict__)
	assert response.status_code == 201
	assert response.get_json() == category.__dict__


def test_handle_category(client, category):
	client.post('/category', json=category.__dict__)
	response = client.get('/category/1')
	assert response.status_code == 200
	assert response.get_json() == category.__dict__
	response = client.put('/category/1', json={'name': 'Updated Category'})
	assert response.status_code == 200
	assert response.get_json()['name'] == 'Updated Category'
	response = client.delete('/category/1')
	assert response.status_code == 204
