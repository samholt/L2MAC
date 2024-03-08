from dataclasses import dataclass
from typing import List


@dataclass
class User:
	id: int
	username: str
	followers: List['User']
	following: List['User']
	tweets: List['Tweet']
	direct_messages: List['DirectMessage']

	def post_tweet(self, tweet):
		self.tweets.append(tweet)

	def reply_to_tweet(self, tweet, reply):
		tweet.replies.append(reply)

	def follow(self, user):
		self.following.append(user)
		user.followers.append(self)

	def send_direct_message(self, user, message):
		dm = DirectMessage(sender=self, receiver=user, message=message)
		self.direct_messages.append(dm)
		user.direct_messages.append(dm)


@dataclass
class Tweet:
	id: int
	user: User
	content: str
	privacy: str
	replies: List['Tweet']
	mentions: List['User']

	def set_privacy(self, privacy):
		self.privacy = privacy

	def add_mention(self, user):
		self.mentions.append(user)


@dataclass
class DirectMessage:
	id: int
	sender: User
	receiver: User
	message: str


@dataclass
class Mention:
	id: int
	user: User
	tweet: Tweet
