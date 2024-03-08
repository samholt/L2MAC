import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={
		'id': '1',
		'name': 'Test User'
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'name': 'Test User'
	}


def test_create_recipe(client):
	response = client.post('/recipe', json={
		'id': '1',
		'name': 'Test Recipe'
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'name': 'Test Recipe'
	}


def test_create_review(client):
	response = client.post('/review', json={
		'id': '1',
		'user_id': '1',
		'recipe_id': '1',
		'rating': 5,
		'comment': 'Great recipe!'
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'user_id': '1',
		'recipe_id': '1',
		'rating': 5,
		'comment': 'Great recipe!'
	}
