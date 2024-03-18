import pytest
from app import app, users, posts, trending
from user import User
from post import Post


def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert resp.data == b'Hello, World!'


def test_register():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		assert resp.status_code == 201
		assert resp.get_json() == {'message': 'User registered successfully.'}


def test_login():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		assert 'token' in resp.get_json()


def test_create_post():
	with app.test_client() as c:
		resp = c.post('/post', json={'username': 'test', 'text': 'Hello, World!'})
		assert resp.status_code == 201
		assert resp.get_json() == {'message': 'Post created successfully.'}


def test_delete_post():
	with app.test_client() as c:
		resp = c.delete('/post/0')
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Post deleted successfully.'}


def test_like_post():
	with app.test_client() as c:
		resp = c.post('/post/0/like')
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Post liked successfully.'}


def test_retweet_post():
	with app.test_client() as c:
		resp = c.post('/post/0/retweet')
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Post retweeted successfully.'}


def test_reply_post():
	with app.test_client() as c:
		resp = c.post('/post/0/reply', json={'reply': 'Hello, World!'})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Reply posted successfully.'}


def test_follow_user():
	with app.test_client() as c:
		resp = c.post('/user/test/follow', json={'follower_username': 'test'})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'User followed successfully.'}


def test_unfollow_user():
	with app.test_client() as c:
		resp = c.post('/user/test/unfollow', json={'follower_username': 'test'})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'User unfollowed successfully.'}


def test_block_user():
	with app.test_client() as c:
		resp = c.post('/user/test/block', json={'blocker_username': 'test'})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'User blocked successfully.'}


def test_unblock_user():
	with app.test_client() as c:
		resp = c.post('/user/test/unblock', json={'blocker_username': 'test'})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'User unblocked successfully.'}


def test_get_notifications():
	with app.test_client() as c:
		resp = c.get('/user/test/notifications')
		assert resp.status_code == 200
		assert 'notifications' in resp.get_json()


def test_get_trending_hashtags():
	with app.test_client() as c:
		resp = c.get('/trending/hashtags')
		assert resp.status_code == 200
		assert 'trending_hashtags' in resp.get_json()


def test_get_trending_topics():
	with app.test_client() as c:
		resp = c.get('/trending/topics')
		assert resp.status_code == 200
		assert 'trending_topics' in resp.get_json()


def test_get_user_recommendations():
	with app.test_client() as c:
		resp = c.get('/user/test/recommendations')
		assert resp.status_code == 200
		assert 'recommendations' in resp.get_json()

