import pytest
from models import User, Post, Reply, db
from app import app


def setup_function():
	with app.app_context():
		db.create_all()

def teardown_function():
	with app.app_context():
		db.session.remove()
		db.drop_all()

def test_create_post():
	with app.app_context():
		with app.test_client() as client:
			new_user = User(email='test@test.com', username='test')
			new_user.set_password('test')
			db.session.add(new_user)
			db.session.commit()
			response = client.post('/post', json={'content': 'Test post', 'user_id': new_user.id})
			assert response.status_code == 201
			assert response.get_json()['message'] == 'Post created successfully'

def test_view_post():
	with app.app_context():
		with app.test_client() as client:
			new_user = User(email='test@test.com', username='test')
			new_user.set_password('test')
			db.session.add(new_user)
			db.session.commit()
			new_post = Post(content='Test post', user_id=new_user.id)
			db.session.add(new_post)
			db.session.commit()
			response = client.get(f'/post/{new_post.id}')
			assert response.status_code == 200
			assert response.get_json()['content'] == new_post.content

def test_delete_post():
	with app.app_context():
		with app.test_client() as client:
			new_user = User(email='test@test.com', username='test')
			new_user.set_password('test')
			db.session.add(new_user)
			db.session.commit()
			new_post = Post(content='Test post', user_id=new_user.id)
			db.session.add(new_post)
			db.session.commit()
			response = client.delete(f'/post/{new_post.id}')
			assert response.status_code == 200
			assert response.get_json()['message'] == 'Post deleted successfully'

def test_like_post():
	with app.app_context():
		with app.test_client() as client:
			new_user = User(email='test@test.com', username='test')
			new_user.set_password('test')
			db.session.add(new_user)
			db.session.commit()
			new_post = Post(content='Test post', user_id=new_user.id)
			db.session.add(new_post)
			db.session.commit()
			response = client.post(f'/post/{new_post.id}/like')
			assert response.status_code == 200
			assert response.get_json()['message'] == 'Post liked successfully'
			assert new_post.likes == 1

def test_retweet_post():
	with app.app_context():
		with app.test_client() as client:
			new_user = User(email='test@test.com', username='test')
			new_user.set_password('test')
			db.session.add(new_user)
			db.session.commit()
			new_post = Post(content='Test post', user_id=new_user.id)
			db.session.add(new_post)
			db.session.commit()
			response = client.post(f'/post/{new_post.id}/retweet')
			assert response.status_code == 200
			assert response.get_json()['message'] == 'Post retweeted successfully'
			assert new_post.retweets == 1

def test_reply_post():
	with app.app_context():
		with app.test_client() as client:
			new_user = User(email='test@test.com', username='test')
			new_user.set_password('test')
			db.session.add(new_user)
			db.session.commit()
			new_post = Post(content='Test post', user_id=new_user.id)
			db.session.add(new_post)
			db.session.commit()
			response = client.post(f'/post/{new_post.id}/reply', json={'content': 'Test reply', 'user_id': new_user.id})
			assert response.status_code == 201
			assert response.get_json()['message'] == 'Reply posted successfully'
			assert len(new_post.replies) == 1
			assert new_post.replies[0].content == 'Test reply'
