import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'name': 'John', 'email': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'John', 'email': 'john@example.com'}


def test_create_recipe(client):
	response = client.post('/recipe', json={'name': 'Pasta', 'ingredients': [{'name': 'Pasta'}, {'name': 'Tomato Sauce'}], 'instructions': [{'step': 'Boil pasta'}, {'step': 'Add sauce'}], 'images': [], 'categories': [{'name': 'Italian'}, {'name': 'Dinner'}]})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'Pasta', 'ingredients': [{'name': 'Pasta'}, {'name': 'Tomato Sauce'}], 'instructions': [{'step': 'Boil pasta'}, {'step': 'Add sauce'}], 'images': [], 'categories': [{'name': 'Italian'}, {'name': 'Dinner'}]}


def test_update_recipe(client):
	client.post('/recipe', json={'name': 'Pasta', 'ingredients': [{'name': 'Pasta'}, {'name': 'Tomato Sauce'}], 'instructions': [{'step': 'Boil pasta'}, {'step': 'Add sauce'}], 'images': [], 'categories': [{'name': 'Italian'}, {'name': 'Dinner'}]})
	response = client.put('/recipe/Pasta', json={'ingredients': [{'name': 'Pasta'}, {'name': 'Tomato Sauce'}, {'name': 'Cheese'}]})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Pasta', 'ingredients': [{'name': 'Pasta'}, {'name': 'Tomato Sauce'}, {'name': 'Cheese'}], 'instructions': [{'step': 'Boil pasta'}, {'step': 'Add sauce'}], 'images': [], 'categories': [{'name': 'Italian'}, {'name': 'Dinner'}]}


def test_delete_recipe(client):
	client.post('/recipe', json={'name': 'Pasta', 'ingredients': [{'name': 'Pasta'}, {'name': 'Tomato Sauce'}], 'instructions': [{'step': 'Boil pasta'}, {'step': 'Add sauce'}], 'images': [], 'categories': [{'name': 'Italian'}, {'name': 'Dinner'}]})
	response = client.delete('/recipe/Pasta')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe deleted'}
