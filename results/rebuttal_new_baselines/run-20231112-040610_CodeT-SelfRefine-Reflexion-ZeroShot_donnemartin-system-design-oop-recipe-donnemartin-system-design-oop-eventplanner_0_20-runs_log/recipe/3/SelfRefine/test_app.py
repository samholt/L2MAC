import pytest
import app

@pytest.fixture(scope='module')
def test_client():
	app.app.config['TESTING'] = True
	app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	test_client = app.app.test_client()
	ctx = app.app.app_context()
	ctx.push()
	app.db.create_all()
	yield test_client
	ctx.pop()


def test_create_user(test_client):
	response = test_client.post('/user', json={'name': 'Test User', 'email': 'test@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'Test User', 'email': 'test@example.com', 'recipes': [], 'favorites': []}


def test_create_recipe(test_client):
	response = test_client.post('/recipe', json={'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2'], 'user_id': 1})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2'], 'user_id': 1}
