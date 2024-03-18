import pytest
from user import User
from post import Post

def test_create_post():
	db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(db)
	post = Post(user, 'Hello, world!')
	post.create(db)
	assert post in db[user.email].posts

def test_delete_post():
	db = {}
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.register(db)
	post = Post(user, 'Hello, world!')
	post.create(db)
	post.delete(db)
	assert post not in db[user.email].posts
