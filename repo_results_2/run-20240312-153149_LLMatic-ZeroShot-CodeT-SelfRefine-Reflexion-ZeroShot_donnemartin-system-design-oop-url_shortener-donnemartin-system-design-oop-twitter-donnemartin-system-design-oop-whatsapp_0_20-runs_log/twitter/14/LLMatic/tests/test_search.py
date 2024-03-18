import pytest
from models import User, Post, users_db, posts_db
from app import app


def setup_function():
	users_db.clear()
	posts_db.clear()
	users_db['testuser'] = User('test@test.com', 'testuser', 'testpassword', bio='test bio')
	posts_db[0] = Post('test post', None, 'testuser')


def test_search():
	with app.test_client() as client:
		response = client.get('/search?q=test')
		assert response.status_code == 200
		assert response.get_json() == {'users': ['testuser'], 'posts': [0]}
