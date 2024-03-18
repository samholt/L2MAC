import pytest
import jwt
from models import User, Post, Message, Notification, users_db, posts_db, messages_db, notifications_db
from views import views
from app import app


def test_notifications():
	with app.test_client() as client:
		client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		client.post('/register', json={'email': 'test2@test.com', 'username': 'test2', 'password': 'test2'})
		client.post('/follow/test2', json={'username': 'test', 'password': 'test'})
		client.post('/post', json={'username': 'test', 'password': 'test', 'text': 'Hello, world!'})
		client.post('/post/0/like', json={'username': 'test2', 'password': 'test2'})
		client.post('/message', json={'sender': 'test', 'password': 'test', 'receiver': 'test2', 'text': 'Hello, test2!'})
		response = client.post('/notifications', json={'username': 'test', 'password': 'test'})
		data = response.get_json()
		assert response.status_code == 200
		assert len(data['notifications']) == 3
		assert data['notifications'][0]['notification_type'] == 'follow'
		assert data['notifications'][1]['notification_type'] == 'post'
		assert data['notifications'][2]['notification_type'] == 'message'

