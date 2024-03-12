import pytest
from app import app
from user import User
from mock_db import MockDB
from contact import Contact
from message import Message

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_send_message(client):
	db = MockDB()
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	db.add(user1.email, user1)
	db.add(user2.email, user2)
	response = client.post('/login', json={'email': 'user1@example.com', 'password': 'password1'})
	assert response.status_code == 200
	assert user1.get_online_status() == True
	response = client.post('/send_message', json={'sender': 'user1@example.com', 'password': 'password1', 'receiver': 'user2@example.com', 'content': 'Hello, user2!'})
	assert response.status_code == 200
	assert response.data == b'Message sent'
	assert len(user2.get_message_queue()) == 0

	user2.set_online_status(False)
	response = client.post('/send_message', json={'sender': 'user1@example.com', 'password': 'password1', 'receiver': 'user2@example.com', 'content': 'Hello, user2!'})
	assert response.status_code == 200
	assert response.data == b'Message sent'
	assert len(user2.get_message_queue()) == 1

def test_status(client):
	db = MockDB()
	user1 = User('user1@example.com', 'password1')
	db.add(user1.email, user1)
	response = client.get('/status', json={'email': 'user1@example.com'})
	assert response.status_code == 200
	assert user1.get_online_status() == True
	user1.set_online_status(False)
	response = client.get('/status', json={'email': 'user1@example.com'})
	assert response.status_code == 200
	assert user1.get_online_status() == False
