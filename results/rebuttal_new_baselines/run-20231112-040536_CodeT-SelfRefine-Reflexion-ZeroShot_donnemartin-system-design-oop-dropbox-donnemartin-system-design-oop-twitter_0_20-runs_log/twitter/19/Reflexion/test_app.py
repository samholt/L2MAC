import pytest
from app import app, db
from models import User, Post, Follow

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

@pytest.mark.usefixtures('client', 'init_database')
class TestApp:
	def test_register(self, client):
		response = client.post('/register', json={'id': 1, 'username': 'test', 'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 201

	def test_login(self, client):
		response = client.post('/login', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200

	def test_post(self, client):
		response = client.post('/post', json={'id': 1, 'user_id': 1, 'content': 'Hello, World!'})
		assert response.status_code == 201

	def test_follow(self, client):
		response = client.post('/follow', json={'follower_id': 1, 'followed_id': 2})
		assert response.status_code == 200

	def test_unfollow(self, client):
		response = client.post('/unfollow', json={'follower_id': 1, 'followed_id': 2})
		assert response.status_code == 200
