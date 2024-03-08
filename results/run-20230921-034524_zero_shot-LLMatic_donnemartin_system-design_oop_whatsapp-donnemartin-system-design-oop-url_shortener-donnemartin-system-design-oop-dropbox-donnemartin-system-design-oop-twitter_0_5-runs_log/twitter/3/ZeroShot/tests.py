import pytest
from models import User, Tweet, DirectMessage, Mention
from controllers import UserController, TweetController, DirectMessageController, MentionController


def test_follow():
	user1 = User(id=1, username='user1', followers=[], following=[])
	user2 = User(id=2, username='user2', followers=[], following=[])
	UserController().follow(user1, user2)
	assert user1.following == [user2.id]
	assert user2.followers == [user1.id]


def test_post_tweet():
	user = User(id=1, username='user1', followers=[], following=[])
	tweet = TweetController().post_tweet(user, 'Hello, world!', False)
	assert tweet.content == 'Hello, world!'


def test_reply_to_tweet():
	user = User(id=1, username='user1', followers=[], following=[])
	tweet = TweetController().post_tweet(user, 'Hello, world!', False)
	reply = TweetController().reply_to_tweet(user, tweet, 'Hello, user1!')
	assert reply.content == 'Hello, user1!'
	assert reply.id in tweet.replies


def test_send_direct_message():
	user1 = User(id=1, username='user1', followers=[], following=[])
	user2 = User(id=2, username='user2', followers=[], following=[])
	message = DirectMessageController().send_direct_message(user1, user2, 'Hello, user2!')
	assert message.content == 'Hello, user2!'


def test_mention_user():
	user = User(id=1, username='user1', followers=[], following=[])
	tweet = TweetController().post_tweet(user, 'Hello, world!', False)
	mention = MentionController().mention_user(user, tweet)
	assert mention.user_id == user.id
	assert mention.tweet_id == tweet.id
