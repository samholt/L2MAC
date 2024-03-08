from models import User, Tweet
from views import UserView, TweetView, DirectMessageView, MentionView


def test_follow_user():
	user1 = User(id=0, username='user1', following=[])
	user2 = User(id=1, username='user2', following=[])
	user_view = UserView()
	user_view.follow_user(user1, user2)
	assert user2.id in user1.following


def test_post_tweet():
	user = User(id=0, username='user', following=[])
	tweet_view = TweetView()
	tweet = tweet_view.post_tweet(user, 'Hello, world!', 'public')
	assert tweet.content == 'Hello, world!'


def test_reply_to_tweet():
	user = User(id=0, username='user', following=[])
	tweet_view = TweetView()
	tweet = tweet_view.post_tweet(user, 'Hello, world!', 'public')
	reply = tweet_view.reply_to_tweet(user, tweet, 'Hello, user!')
	assert reply in tweet.replies


def test_send_message():
	user1 = User(id=0, username='user1', following=[])
	user2 = User(id=1, username='user2', following=[])
	dm_view = DirectMessageView()
	message = dm_view.send_message(user1, user2, 'Hello, user2!')
	assert message.content == 'Hello, user2!'


def test_mention_user():
	user = User(id=0, username='user', following=[])
	tweet_view = TweetView()
	tweet = tweet_view.post_tweet(user, 'Hello, world!', 'public')
	mention_view = MentionView()
	mention = mention_view.mention_user(user, tweet)
	assert mention.tweet_id == tweet.id
