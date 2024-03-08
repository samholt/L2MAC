import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'name': 'John Doe', 'email': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_create_recipe(client):
	client.post('/user', json={'name': 'John Doe', 'email': 'john@example.com'})
	response = client.post('/recipe', json={'title': 'Pasta', 'instructions': 'Boil water. Cook pasta.', 'ingredients': 'Pasta, Water', 'user_email': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Recipe created successfully'}


def test_create_review(client):
	client.post('/user', json={'name': 'John Doe', 'email': 'john@example.com'})
	client.post('/recipe', json={'title': 'Pasta', 'instructions': 'Boil water. Cook pasta.', 'ingredients': 'Pasta, Water', 'user_email': 'john@example.com'})
	response = client.post('/review', json={'user_email': 'john@example.com', 'recipe_title': 'Pasta', 'comment': 'Delicious!'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Review created successfully'}
