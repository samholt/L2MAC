import pytest
import app
from app import db, User, Recipe

@pytest.fixture(scope='module')
def setup_module():
	app.app.config['TESTING'] = True
	app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	db.create_all()

@pytest.fixture
def client():
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={
		'id': '1',
		'name': 'Test User'
	})
	assert response.status_code == 201
	assert response.get_json() == '1'


def test_create_recipe(client):
	response = client.post('/recipe', json={
		'id': '1',
		'name': 'Test Recipe',
		'user_id': '1'
	})
	assert response.status_code == 201
	assert response.get_json() == '1'


def test_get_user(client):
	response = client.get('/user/1')
	assert response.status_code == 200
	assert response.get_json() == '1'


def test_get_recipe(client):
	response = client.get('/recipe/1')
	assert response.status_code == 200
	assert response.get_json() == '1'
