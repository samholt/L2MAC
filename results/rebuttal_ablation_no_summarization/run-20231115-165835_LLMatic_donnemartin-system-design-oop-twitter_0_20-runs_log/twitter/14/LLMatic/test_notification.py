import pytest
from user import User
from post import Post
from notification import Notification

def test_notification():
	user1 = User('test1@test.com', 'test1', 'password1')
	user2 = User('test2@test.com', 'test2', 'password2')
	post = Post(user1, 'Hello world!')
	notification = Notification(user2, 'like', post)

	assert notification.user == user2
	assert notification.type == 'like'
	assert notification.post == post
	assert notification.viewed == False

	viewed_notification = notification.view_notification()
	assert viewed_notification.viewed == True

