import pytest
import random
import string
from oms import app
from database import Database
from user import User
from post import Post
from message import Message
from notification import Notification
from trending import Trending


def random_string(length=10):
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def test_user_registration():
	with app.test_client() as client:
		username = random_string()
		email = f'{random_string()}@example.com'
		password = random_string()
		response = client.post('/register', json={'id': 1, 'username': username, 'email': email, 'password': password})
		assert response.status_code == 201


def test_user_authentication():
	with app.test_client() as client:
		username = random_string()
		email = f'{random_string()}@example.com'
		password = random_string()
		client.post('/register', json={'id': 2, 'username': username, 'email': email, 'password': password})
		response = client.post('/login', json={'id': 2, 'password': password})
		assert response.status_code == 200


def test_create_post():
	with app.test_client() as client:
		client.post('/register', json={'id': 3, 'username': random_string(), 'email': f'{random_string()}@example.com', 'password': random_string()})
		response = client.post('/post', json={'id': 1, 'user_id': 3, 'content': random_string(280)})
		assert response.status_code == 201


def test_send_message():
	with app.test_client() as client:
		client.post('/register', json={'id': 4, 'username': random_string(), 'email': f'{random_string()}@example.com', 'password': random_string()})
		client.post('/register', json={'id': 5, 'username': random_string(), 'email': f'{random_string()}@example.com', 'password': random_string()})
		response = client.post('/message', json={'id': 1, 'sender_id': 4, 'receiver_id': 5, 'content': random_string(100)})
		assert response.status_code == 201


def test_create_notification():
	with app.test_client() as client:
		client.post('/register', json={'id': 6, 'username': random_string(), 'email': f'{random_string()}@example.com', 'password': random_string()})
		response = client.post('/notification', json={'id': 1, 'user_id': 6, 'content': random_string(100)})
		assert response.status_code == 201


def test_add_trending():
	with app.test_client() as client:
		response = client.post('/trending', json={'id': 1, 'topic': random_string(), 'mentions': random.randint(1, 100)})
		assert response.status_code == 201
