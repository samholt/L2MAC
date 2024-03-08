from main import app, create_account, submit_recipe, rate_recipe, admin_manage_recipes
import json

app.testing = True
client = app.test_client()

def test_home():
	response = client.get('/')
	assert response.status_code == 200

def test_create_account():
	data = {'username': 'test', 'password': 'test'}
	response = client.post('/create_account', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 200

def test_submit_recipe():
	data = {'username': 'test', 'recipe_name': 'test_recipe'}
	response = client.post('/submit_recipe', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 200

def test_rate_recipe():
	data = {'username': 'test', 'recipe_name': 'test_recipe', 'rating': 5}
	response = client.post('/rate_recipe', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 200

def test_admin_manage_recipes():
	data = {'recipe_id': 'test_recipe', 'action': 'remove'}
	response = client.post('/admin_manage_recipes', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 200
