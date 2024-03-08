import pytest
from user import User
from tweet import Tweet


def test_user():
	user = User('testuser')
	assert user.username == 'testuser'
	assert user.tweets == []
	assert user.following == []
	assert user.followers == []
	assert user.direct_messages == []

	tweet = user.post_tweet('Hello, world!')
	assert isinstance(tweet, Tweet)
	assert tweet in user.tweets

	reply = user.reply_to_tweet(tweet, 'Hello, testuser!')
	assert isinstance(reply, Tweet)
	assert reply in user.tweets

	message = user.send_direct_message(user, 'Hello!')
	assert message in user.direct_messages

	user.follow(user)
	assert user in user.following
	assert user in user.followers

	mention = user.mention(user, 'Check this out, @testuser!')
	assert mention in user.tweets
	assert user in mention.mentions
