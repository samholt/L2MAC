import pytest
import app
from app import User, Recipe, Review

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.User.query.delete()
	app.Recipe.query.delete()
	app.Review.query.delete()
	app.db.session.commit()

@pytest.mark.usefixtures('reset_db')
def test_create_user(client):
	user = User(id='1', name='Test User', recipes=[], favorites=[], followers=[])
	response = client.post('/user', json=user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == user.__dict__

@pytest.mark.usefixtures('reset_db')
def test_update_user(client):
	user = User(id='1', name='Test User', recipes=[], favorites=[], followers=[])
	client.post('/user', json=user.__dict__)
	user.name = 'Updated User'
	response = client.put('/user/1', json=user.__dict__)
	assert response.status_code == 200
	assert response.get_json() == user.__dict__

@pytest.mark.usefixtures('reset_db')
def test_delete_user(client):
	user = User(id='1', name='Test User', recipes=[], favorites=[], followers=[])
	client.post('/user', json=user.__dict__)
	response = client.delete('/user/1')
	assert response.status_code == 204

@pytest.mark.usefixtures('reset_db')
def test_create_recipe(client):
	recipe = Recipe(id='1', name='Test Recipe', ingredients=[], instructions=[], images=[], categories=[], user_id='1')
	response = client.post('/recipe', json=recipe.__dict__)
	assert response.status_code == 201
	assert response.get_json() == recipe.__dict__

@pytest.mark.usefixtures('reset_db')
def test_update_recipe(client):
	recipe = Recipe(id='1', name='Test Recipe', ingredients=[], instructions=[], images=[], categories=[], user_id='1')
	client.post('/recipe', json=recipe.__dict__)
	recipe.name = 'Updated Recipe'
	response = client.put('/recipe/1', json=recipe.__dict__)
	assert response.status_code == 200
	assert response.get_json() == recipe.__dict__

@pytest.mark.usefixtures('reset_db')
def test_delete_recipe(client):
	recipe = Recipe(id='1', name='Test Recipe', ingredients=[], instructions=[], images=[], categories=[], user_id='1')
	client.post('/recipe', json=recipe.__dict__)
	response = client.delete('/recipe/1')
	assert response.status_code == 204

@pytest.mark.usefixtures('reset_db')
def test_create_review(client):
	review = Review(id='1', user_id='1', recipe_id='1', rating=5, comment='Great recipe!')
	response = client.post('/review', json=review.__dict__)
	assert response.status_code == 201
	assert response.get_json() == review.__dict__

@pytest.mark.usefixtures('reset_db')
def test_update_review(client):
	review = Review(id='1', user_id='1', recipe_id='1', rating=5, comment='Great recipe!')
	client.post('/review', json=review.__dict__)
	review.comment = 'Updated comment'
	response = client.put('/review/1', json=review.__dict__)
	assert response.status_code == 200
	assert response.get_json() == review.__dict__

@pytest.mark.usefixtures('reset_db')
def test_delete_review(client):
	review = Review(id='1', user_id='1', recipe_id='1', rating=5, comment='Great recipe!')
	client.post('/review', json=review.__dict__)
	response = client.delete('/review/1')
	assert response.status_code == 204
