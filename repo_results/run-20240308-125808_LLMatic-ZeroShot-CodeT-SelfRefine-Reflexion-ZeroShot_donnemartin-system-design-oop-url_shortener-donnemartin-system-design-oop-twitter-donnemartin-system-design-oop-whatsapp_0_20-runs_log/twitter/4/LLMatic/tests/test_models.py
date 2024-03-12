from datetime import datetime
from models import User, Comment, Message, Notification, TrendingTopic


def test_user_creation():
	user = User('1', 'testuser', 'testpassword')
	assert user.id == '1'
	assert user.username == 'testuser'
	assert user.password == 'testpassword'


def test_comment_creation():
	comment = Comment('1', '1', 'test comment')
	assert comment.id == '1'
	assert comment.user_id == '1'
	assert comment.text == 'test comment'


def test_message_creation():
	message = Message('1', '1', '2', 'test message')
	assert message.id == '1'
	assert message.sender_id == '1'
	assert message.receiver_id == '2'
	assert message.text == 'test message'
	assert isinstance(message.timestamp, datetime)


def test_message_deletion():
	message = Message('1', '1', '2', 'test message')
	message.delete()
	# assert that the message has been deleted
	# this will depend on how the delete method is implemented


def test_notification_creation():
	notification = Notification('1', '1', 'like')
	assert notification.id == '1'
	assert notification.user_id == '1'
	assert notification.type == 'like'
	assert isinstance(notification.timestamp, datetime)


def test_trending_topic_creation():
	trending_topic = TrendingTopic('1', '#test', 1)
	assert trending_topic.id == '1'
	assert trending_topic.hashtag == '#test'
	assert trending_topic.count == 1
	assert isinstance(trending_topic.timestamp, datetime)


def test_trending_topic_count_update():
	trending_topic = TrendingTopic('1', '#test', 1)
	trending_topic.update_count(2)
	assert trending_topic.count == 2
