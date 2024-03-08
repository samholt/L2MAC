import pytest
from flask import json
from models import User, users_db, Post, posts_db, Like, likes_db
from app import app


def setup_module():
	test_user = User('test_user', 'test@test.com', 'test_password')
	users_db['test_user'] = test_user
	test_post = Post('test_post', test_user, 'test content', None)
	posts_db['test_post'] = test_post


def test_like_post():
	with app.test_client() as client:
		response = client.post('/like_post', json={'username': 'test_user', 'post_id': 'test_post', 'like_id': 'test_like'})
		data = json.loads(response.data)
		assert response.status_code == 201
		assert data['message'] == 'Post liked successfully'
		assert 'test_like' in likes_db

