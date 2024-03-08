from models import User, Tweet, DirectMessage, Mention


class UserController:
	def __init__(self):
		self.users = []

	def create_user(self, username):
		user_id = len(self.users) + 1
		user = User(user_id, username, [])
		self.users.append(user)
		return user

	def follow_user(self, user_id, follower_id):
		user = self.users[user_id - 1]
		user.followers.append(follower_id)


class TweetController:
	def __init__(self):
		self.tweets = []

	def create_tweet(self, user_id, content, privacy):
		tweet_id = len(self.tweets) + 1
		tweet = Tweet(tweet_id, user_id, content, [], [], privacy)
		self.tweets.append(tweet)
		return tweet

	def reply_to_tweet(self, user_id, tweet_id, content):
		reply_id = len(self.tweets) + 1
		reply = Tweet(reply_id, user_id, content, [], [], 'public')
		self.tweets.append(reply)
		original_tweet = self.tweets[tweet_id - 1]
		original_tweet.replies.append(reply_id)
		return reply

	def get_trending_tweets(self):
		# For simplicity, we'll just return the 5 most recent tweets
		return self.tweets[-5:]


class DirectMessageController:
	def __init__(self):
		self.direct_messages = []

	def send_direct_message(self, sender_id, receiver_id, content):
		message_id = len(self.direct_messages) + 1
		message = DirectMessage(message_id, sender_id, receiver_id, content)
		self.direct_messages.append(message)
		return message


class MentionController:
	def __init__(self):
		self.mentions = []

	def create_mention(self, user_id, tweet_id):
		mention_id = len(self.mentions) + 1
		mention = Mention(mention_id, user_id, tweet_id)
		self.mentions.append(mention)
		tweet = self.tweets[tweet_id - 1]
		tweet.mentions.append(mention_id)
		return mention
