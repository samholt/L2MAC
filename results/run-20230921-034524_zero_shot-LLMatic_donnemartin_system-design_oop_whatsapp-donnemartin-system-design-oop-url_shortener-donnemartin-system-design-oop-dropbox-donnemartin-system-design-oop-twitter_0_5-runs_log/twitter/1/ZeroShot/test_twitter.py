from models import User, Tweet, DirectMessage, Mention
from controllers import UserController, TweetController, DirectMessageController, MentionController


def test_user_creation():
	user_controller = UserController()
	user = user_controller.create_user('testuser')
	assert user.username == 'testuser'


def test_tweet_creation():
	tweet_controller = TweetController()
	tweet = tweet_controller.create_tweet(1, 'test tweet', 'public')
	assert tweet.content == 'test tweet'


def test_direct_message_creation():
	direct_message_controller = DirectMessageController()
	message = direct_message_controller.send_direct_message(1, 2, 'test message')
	assert message.content == 'test message'


def test_mention_creation():
	mention_controller = MentionController()
	mention = mention_controller.create_mention(1, 1)
	assert mention.user_id == 1
	assert mention.tweet_id == 1
