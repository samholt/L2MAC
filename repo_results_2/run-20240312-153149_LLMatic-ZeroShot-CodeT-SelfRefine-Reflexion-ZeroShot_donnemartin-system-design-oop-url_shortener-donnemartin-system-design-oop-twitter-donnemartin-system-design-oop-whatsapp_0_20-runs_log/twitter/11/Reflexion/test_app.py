import pytest
from app import app, db
from models import User, Post, Comment

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def init_database():
	db.create_all()
	yield
	db.drop_all()

def test_register(client, init_database):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

def test_login(client, init_database):
	user = User(username='test', email='test@test.com', password='test')
	db.session.add(user)
	db.session.commit()
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()

def test_post(client, init_database):
	user = User(username='test', email='test@test.com', password='test')
	db.session.add(user)
	db.session.commit()
	response = client.post('/post', json={'user_id': user.id, 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Post created successfully'}

def test_comment(client, init_database):
	user = User(username='test', email='test@test.com', password='test')
	post = Post(user_id=user.id, content='Hello, world!')
	db.session.add(user)
	db.session.add(post)
	db.session.commit()
	response = client.post('/comment', json={'post_id': post.id, 'user_id': user.id, 'content': 'Nice post!'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Comment added successfully'}
