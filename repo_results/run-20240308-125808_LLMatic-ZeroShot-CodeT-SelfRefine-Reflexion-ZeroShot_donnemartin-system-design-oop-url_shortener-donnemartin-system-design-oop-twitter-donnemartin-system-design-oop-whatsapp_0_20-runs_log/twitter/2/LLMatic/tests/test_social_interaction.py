import pytest
from models import User, Post, Message
from views import views


def test_follow():
	views.users = {'user1': User('user1', 'user1', 'password'), 'user2': User('user2', 'user2', 'password')}
	response = views.follow({'email': 'user1', 'to_follow': 'user2'})
	assert response[1] == 200
	assert 'user2' in views.users['user1'].following
	assert 'user1' in views.users['user2'].followers


def test_unfollow():
	views.users = {'user1': User('user1', 'user1', 'password'), 'user2': User('user2', 'user2', 'password')}
	views.users['user1'].following.append('user2')
	views.users['user2'].followers.append('user1')
	response = views.unfollow({'email': 'user1', 'to_unfollow': 'user2'})
	assert response[1] == 200
	assert 'user2' not in views.users['user1'].following
	assert 'user1' not in views.users['user2'].followers


def test_send_message():
	views.users = {'user1': User('user1', 'user1', 'password'), 'user2': User('user2', 'user2', 'password')}
	response = views.send_message({'sender': 'user1', 'receiver': 'user2', 'content': 'Hello, user2!'})
	assert response[1] == 200
	message = views.messages[0]
	assert message.sender == views.users['user1']
	assert message.receiver == views.users['user2']
	assert message.content == 'Hello, user2!'


def test_get_message():
	views.users = {'user1': User('user1', 'user1', 'password'), 'user2': User('user2', 'user2', 'password')}
	views.messages = {0: Message(views.users['user1'], views.users['user2'], 'Hello, user2!')}
	response = views.get_message(0, {'email': 'user1'})
	assert response[1] == 200
	assert response[0]['sender'] == 'user1'
	assert response[0]['receiver'] == 'user2'
	assert response[0]['content'] == 'Hello, user2!'

