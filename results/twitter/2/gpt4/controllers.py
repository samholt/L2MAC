from models import User, Tweet, DirectMessage, Mention


class UserController:
	def follow(self, user: User, other_user: User):
		user.following.append(other_user.id)


class TweetController:
	def post_tweet(self, user: User, content: str, privacy: str):
		tweet = Tweet(id=0, user_id=user.id, content=content, replies=[], privacy=privacy)
		return tweet

	def reply_to_tweet(self, user: User, tweet: Tweet, content: str):
		reply = Tweet(id=0, user_id=user.id, content=content, replies=[], privacy=tweet.privacy)
		tweet.replies.append(reply)
		return reply

	def get_trending_tweets(self):
		# Placeholder for getting trending tweets
		return []


class DirectMessageController:
	def send_message(self, sender: User, receiver: User, content: str):
		message = DirectMessage(id=0, sender_id=sender.id, receiver_id=receiver.id, content=content)
		return message


class MentionController:
	def mention_user(self, user: User, tweet: Tweet):
		mention = Mention(id=0, user_id=user.id, tweet_id=tweet.id)
		return mention
