import pytest
from models.user import User
from models.tweet import Tweet
from models.conversation import Conversation
from controllers.user_controller import UserController
from controllers.tweet_controller import TweetController
from controllers.conversation_controller import ConversationController


def test_conversation_creation():
	user_controller = UserController()
	tweet_controller = TweetController()
	conversation_controller = ConversationController()
	user = user_controller.create_user('testuser', 'testpassword')
	tweet1 = tweet_controller.create_tweet('Hello, world!', user, 'public')
	tweet2 = tweet_controller.create_reply('Hello, reply!', user, 'public', tweet1)
	conversation = conversation_controller.create_conversation([tweet1, tweet2])
	assert conversation.tweets == [tweet1, tweet2]
