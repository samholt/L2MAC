from models.tweet import Tweet


class TweetController:
	def __init__(self):
		self.tweets = []

	def create_tweet(self, content: str, poster, privacy: str):
		tweet = Tweet(content, poster, privacy)
		self.tweets.append(tweet)
		return tweet

	def create_reply(self, content: str, poster, privacy: str, original_tweet):
		reply = Tweet(content, poster, privacy)
		reply.original_tweet = original_tweet
		self.tweets.append(reply)
		return reply

	def mention_user(self, tweet_id: int, user):
		tweet = self.get_tweet(tweet_id)
		if tweet and user:
			tweet.mentions.append(user)
			return tweet
		return None

	def get_tweet(self, id: int):
		if id < len(self.tweets):
			return self.tweets[id]
		return None

	def update_tweet(self, id: int, new_content: str):
		tweet = self.get_tweet(id)
		if tweet:
			tweet.content = new_content
			return tweet
		return None

	def delete_tweet(self, id: int):
		tweet = self.get_tweet(id)
		if tweet:
			self.tweets.remove(tweet)
			return tweet
		return None
