from models import User, Tweet, DirectMessage, Mention


class UserController:
	def follow(self, follower: User, followee: User):
		follower.following.append(followee.id)
		followee.followers.append(follower.id)


class TweetController:
	def post_tweet(self, user: User, content: str, is_private: bool):
		tweet = Tweet(id=generate_id(), user_id=user.id, content=content, replies=[], is_private=is_private)
		return tweet

	def reply_to_tweet(self, user: User, tweet: Tweet, content: str):
		reply = Tweet(id=generate_id(), user_id=user.id, content=content, replies=[], is_private=tweet.is_private)
		tweet.replies.append(reply.id)
		return reply

	def get_trending_tweets(self):
		# This is a placeholder. In a real application, we would implement this method based on the application's business logic.
		return []


class DirectMessageController:
	def send_direct_message(self, sender: User, receiver: User, content: str):
		message = DirectMessage(id=generate_id(), sender_id=sender.id, receiver_id=receiver.id, content=content)
		return message


class MentionController:
	def mention_user(self, user: User, tweet: Tweet):
		mention = Mention(id=generate_id(), user_id=user.id, tweet_id=tweet.id)
		return mention
