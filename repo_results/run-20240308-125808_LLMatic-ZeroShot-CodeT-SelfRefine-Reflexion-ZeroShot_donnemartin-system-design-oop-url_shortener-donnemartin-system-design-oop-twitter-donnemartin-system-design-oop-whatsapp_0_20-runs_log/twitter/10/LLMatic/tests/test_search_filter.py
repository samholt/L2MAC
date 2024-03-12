import pytest
from models import User, Post, db
from app import app


def setup_module(module):
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
	app.app_context().push()
	db.create_all()

	user1 = User(email='user1@example.com', username='user1')
	user1.set_password('password')
	db.session.add(user1)

	user2 = User(email='user2@example.com', username='user2')
	user2.set_password('password')
	db.session.add(user2)

	post1 = Post(content='Hello #world!', user_id=1)
	db.session.add(post1)

	post2 = Post(content='Hello @user1', user_id=2)
	db.session.add(post2)

	db.session.commit()


def teardown_module(module):
	db.session.remove()
	db.drop_all()


def test_search():
	with app.test_client() as client:
		response = client.get('/search?keyword=user1')
		data = response.get_json()
		assert response.status_code == 200
		assert 'user1' in data['users']
		assert 'Hello @user1' in data['posts']


def test_filter():
	with app.test_client() as client:
		response = client.get('/filter?filter_type=hashtags&keyword=world')
		data = response.get_json()
		assert response.status_code == 200
		assert 'Hello #world!' in data['posts']

		response = client.get('/filter?filter_type=mentions&keyword=user1')
		data = response.get_json()
		assert response.status_code == 200
		assert 'Hello @user1' in data['posts']

		response = client.get('/filter?filter_type=trending&keyword=')
		data = response.get_json()
		assert response.status_code == 200
		assert data['posts'] == []
