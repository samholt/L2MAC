import pytest
from models import User, Message, users_db, messages_db
from app import app


def setup_function():
	users_db.clear()
	messages_db.clear()
	users_db['testuser'] = User('testuser@test.com', 'testuser', 'testpassword')
	users_db['testuser2'] = User('testuser2@test.com', 'testuser2', 'testpassword2')


def test_send_message():
	with app.test_client() as client:
		response = client.post('/message', json={'sender': 'testuser', 'password': 'testpassword', 'receiver': 'testuser2', 'text': 'Hello, testuser2!'});
		assert response.status_code == 201
		assert response.get_json() == {'message': 'Message sent successfully'}
		assert len(messages_db) == 1
		assert messages_db[0].sender == 'testuser'
		assert messages_db[0].receiver == 'testuser2'
		assert messages_db[0].text == 'Hello, testuser2!'
