import pytest
import app
from werkzeug.security import generate_password_hash


def test_register():
	with app.app.test_client() as client:
		response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 201
		assert response.get_json() == {'message': 'User registered successfully!'}
		assert 'test' in app.users
		assert app.users['test']['username'] == 'test'
		assert app.users['test']['email'] == 'test@test.com'
		assert app.users['test']['password'] == generate_password_hash('test', method='sha256')


def test_login():
	with app.app.test_client() as client:
		response = client.post('/login', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert 'token' in response.get_json()


def test_create_post():
	with app.app.test_client() as client:
		response = client.post('/login', json={'username': 'test', 'password': 'test'})
		token = response.get_json()['token']
		response = client.post('/post', json={'content': 'This is a test post.'}, headers={'x-access-token': token})
		assert response.status_code == 201
		assert response.get_json() == {'message': 'Post created successfully!'}
		assert len(app.posts) == 1
		assert app.posts[0]['username'] == 'test'
		assert app.posts[0]['content'] == 'This is a test post.'


def test_get_posts():
	with app.app.test_client() as client:
		response = client.post('/login', json={'username': 'test', 'password': 'test'})
		token = response.get_json()['token']
		response = client.get('/posts', headers={'x-access-token': token})
		assert response.status_code == 200
		assert response.get_json() == {'posts': [{'username': 'test', 'content': 'This is a test post.'}]}
