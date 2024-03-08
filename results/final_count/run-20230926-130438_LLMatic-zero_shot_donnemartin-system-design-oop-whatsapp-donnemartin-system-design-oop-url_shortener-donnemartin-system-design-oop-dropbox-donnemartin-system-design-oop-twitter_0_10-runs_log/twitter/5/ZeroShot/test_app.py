import pytest
from app import app, db
from models import User, Post, Like, Follow, Message


@pytest.fixture

def client():
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	with app.test_client() as client:
		yield client


def test_register(client):
	# TODO: Implement test for user registration
	pass


def test_login(client):
	# TODO: Implement test for user login
	pass


def test_profile(client):
	# TODO: Implement test for profile view/edit
	pass


def test_post(client):
	# TODO: Implement test for post creation
	pass


def test_post_detail(client):
	# TODO: Implement test for post view/delete
	pass


def test_like_post(client):
	# TODO: Implement test for post liking
	pass


def test_follow(client):
	# TODO: Implement test for user following
	pass


def test_message(client):
	# TODO: Implement test for direct messaging
	pass


def test_trending(client):
	# TODO: Implement test for trending topics
	pass
