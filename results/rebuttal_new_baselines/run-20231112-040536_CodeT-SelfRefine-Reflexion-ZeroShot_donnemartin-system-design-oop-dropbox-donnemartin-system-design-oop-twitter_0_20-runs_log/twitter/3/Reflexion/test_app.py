import pytest
from app import app, db
from app.models import User, Post

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def init_database():
	db.create_all()
	yield db
	db.drop_all()

def test_register(client, init_database):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

def test_login(client, init_database):
	user = User(username='test', email='test@test.com', password='test')
	init_database.session.add(user)
	init_database.session.commit()
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()

def test_post(client, init_database):
	user = User(username='test', email='test@test.com', password='test')
	init_database.session.add(user)
	init_database.session.commit()
	response = client.post('/post', json={'body': 'Hello, World!', 'user_id': user.id})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Post created successfully'}

def test_get_posts(client, init_database):
	user = User(username='test', email='test@test.com', password='test')
	init_database.session.add(user)
	init_database.session.commit()
	post = Post(body='Hello, World!', user_id=user.id)
	init_database.session.add(post)
	init_database.session.commit()
	response = client.get('/posts')
	assert response.status_code == 200
	assert len(response.get_json()) == 1

def test_delete_post(client, init_database):
	user = User(username='test', email='test@test.com', password='test')
	init_database.session.add(user)
	init_database.session.commit()
	post = Post(body='Hello, World!', user_id=user.id)
	init_database.session.add(post)
	init_database.session.commit()
	response = client.delete(f'/post/{post.id}')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post deleted successfully'}
