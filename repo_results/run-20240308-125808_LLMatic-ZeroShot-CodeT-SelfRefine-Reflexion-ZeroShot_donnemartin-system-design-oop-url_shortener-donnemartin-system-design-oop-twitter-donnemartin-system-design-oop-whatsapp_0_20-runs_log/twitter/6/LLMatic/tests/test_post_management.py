import pytest
from app import create_app
from models import db, User, Post


@pytest.fixture
def client():
	app = create_app()
	app.config['TESTING'] = True

	with app.test_client() as client:
		with app.app_context():
			db.drop_all()
			db.create_all()
			yield client

	with app.app_context():
		db.drop_all()


def test_create_post(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201

	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = response.get_json()['access_token']

	response = client.post('/create_post', json={'content': 'Test post', 'images': 'test.jpg'}, headers={'Authorization': 'Bearer ' + access_token})
	assert response.status_code == 201


def test_delete_post(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201

	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = response.get_json()['access_token']

	response = client.post('/create_post', json={'content': 'Test post', 'images': 'test.jpg'}, headers={'Authorization': 'Bearer ' + access_token})
	assert response.status_code == 201

	response = client.delete('/delete_post/1', headers={'Authorization': 'Bearer ' + access_token})
	assert response.status_code == 200


def test_view_posts(client):
	response = client.get('/view_posts')
	assert response.status_code == 200


def test_search_posts(client):
	response = client.get('/search_posts?keyword=test')
	assert response.status_code == 200
