import pytest
from models import User, Post, users_db, posts_db
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_search(client):
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	post = Post('This is a test post', [], user)
	posts_db[0] = post
	response = client.get('/search', query_string={'keyword': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'results': ['This is a test post']}


def test_filter(client):
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	post = Post('This is a #test post', [], user)
	posts_db[0] = post
	response = client.get('/filter', query_string={'element': '#test'})
	assert response.status_code == 200
	assert response.get_json() == {'results': ['This is a #test post']}
