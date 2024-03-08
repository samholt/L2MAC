import pytest
from app import app
from models import Admin


def test_manage_recipe():
	with app.test_client() as client:
		# Log in as admin
		client.post('/login', json={'username': 'admin', 'password': 'password'})
		# Test manage_recipe route
		response = client.post('/admin/manage_recipe', json={'recipe_id': 1, 'new_data': {'name': 'New Recipe'}})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Recipe updated successfully'}


def test_monitor_site_usage():
	with app.test_client() as client:
		# Log in as admin
		client.post('/login', json={'username': 'admin', 'password': 'password'})
		# Test monitor_site_usage route
		response = client.get('/admin/monitor_site_usage')
		assert response.status_code == 200
		assert response.get_json() == {'total_users': 100, 'total_recipes': 200}

