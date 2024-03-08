import pytest
from main import app


def test_edit_recipe():
	new_recipe_data = {'name': 'new test recipe', 'ingredients': 'new test ingredients', 'instructions': 'new test instructions', 'images': 'new test images', 'categories': 'new test categories'}
	with app.test_client() as client:
		response = client.put('/edit_recipe', json={'username': 'test', 'recipe_name': 'test recipe', 'new_recipe_data': new_recipe_data})
		assert response.status_code == 200
		response = client.put('/edit_recipe', json={'username': 'test', 'recipe_name': 'nonexistent recipe', 'new_recipe_data': new_recipe_data})
		assert response.status_code == 400


def test_delete_recipe():
	with app.test_client() as client:
		response = client.delete('/delete_recipe', json={'username': 'test', 'recipe_name': 'test recipe'})
		assert response.status_code == 200
		response = client.delete('/delete_recipe', json={'username': 'test', 'recipe_name': 'nonexistent recipe'})
		assert response.status_code == 400

