from controllers.user_controller import UserController
from controllers.tweet_controller import TweetController
from controllers.conversation_controller import ConversationController
from controllers.trending_controller import TrendingController
from models.trending import Trending


if __name__ == '__main__':
	# Create users
	user1 = UserController.create_user('user1', 'password1')
	user2 = UserController.create_user('user2', 'password2')

	# User1 follows User2
	UserController.follow_user(user1, user2)

	# User1 posts a tweet
	tweet1 = UserController.post_tweet(user1, 'Hello, world!', 'public')

	# User2 replies to the tweet
	reply1 = UserController.reply_to_tweet(user2, tweet1, 'Hello, user1!')

	# Create a conversation
	ConversationController.create_conversation([user1, user2], [tweet1, reply1])

	# Get trending tweets
	trending = Trending([tweet1, reply1])
	TrendingController.get_trending_tweets(trending)

