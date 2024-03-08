import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={
		'id': '1',
		'name': 'Test User',
		'recipes': [],
		'favorites': []
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'name': 'Test User',
		'recipes': [],
		'favorites': []
	}


def test_create_recipe(client):
	response = client.post('/recipe', json={
		'id': '1',
		'name': 'Test Recipe',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'categories': ['category1', 'category2']
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'name': 'Test Recipe',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'categories': ['category1', 'category2']
	}


def test_create_review(client):
	response = client.post('/review', json={
		'id': '1',
		'user_id': '1',
		'rating': 5,
		'comment': 'Great recipe!'
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'user_id': '1',
		'rating': 5,
		'comment': 'Great recipe!'
	}
