import pytest
from models import User, db
from app import app

def setup_module(module):
	with app.app_context():
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
		db.create_all()

def teardown_module(module):
	with app.app_context():
		db.session.remove()
		db.drop_all()

def test_follow():
	with app.app_context():
		user1 = User(email='user1@example.com', username='user1')
		user1.set_password('password')
		user2 = User(email='user2@example.com', username='user2')
		user2.set_password('password')
		db.session.add(user1)
		db.session.add(user2)
		db.session.commit()
		user1.follow(user2)
		assert user1.is_following(user2)

def test_unfollow():
	with app.app_context():
		user1 = User(email='user1@example.com', username='user1')
		user1.set_password('password')
		user2 = User(email='user2@example.com', username='user2')
		user2.set_password('password')
		db.session.add(user1)
		db.session.add(user2)
		db.session.commit()
		user1.follow(user2)
		user1.unfollow(user2)
		assert not user1.is_following(user2)

def test_cannot_follow_self():
	with app.app_context():
		user1 = User(email='user1@example.com', username='user1')
		user1.set_password('password')
		db.session.add(user1)
		db.session.commit()
		user1.follow(user1)
		assert not user1.is_following(user1)
