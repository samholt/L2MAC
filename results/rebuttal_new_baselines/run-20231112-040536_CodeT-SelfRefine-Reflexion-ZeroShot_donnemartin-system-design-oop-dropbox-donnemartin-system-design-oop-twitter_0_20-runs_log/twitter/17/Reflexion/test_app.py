import pytest
from app import app, db
from models import User, Post, Message, Notification


@pytest.fixture
def client():
	app.config['TESTING'] = True
	client = app.test_client()

	with app.app_context():
		db.create_all()

	yield client

	db.session.remove()
	db.drop_all()


def test_register(client):
	# Test user registration
	pass


def test_login(client):
	# Test user login
	pass


def test_profile(client):
	# Test user profile management
	pass


def test_post(client):
	# Test creating a post
	pass


def test_post_detail(client):
	# Test viewing and deleting a post
	pass


def test_follow(client):
	# Test following a user
	pass


def test_unfollow(client):
	# Test unfollowing a user
	pass


def test_message(client):
	# Test sending a message
	pass


def test_message_detail(client):
	# Test viewing and deleting a message
	pass


def test_notification(client):
	# Test viewing notifications
	pass


def test_trending(client):
	# Test viewing trending topics
	pass


def test_recommendation(client):
	# Test viewing user recommendations
	pass
