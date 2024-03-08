import pytest
from app import app
from models import db, User, Post, Comment, Like, Follow, Message, Notification

@pytest.fixture
def client():
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	with app.test_client() as client:
		yield client

# Write your tests here
