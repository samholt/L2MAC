from user import User
from tweet import Tweet
from conversation import Conversation
from direct_message import DirectMessage
from trending import Trending


if __name__ == '__main__':
	# Create some users
	user1 = User('user1')
	user2 = User('user2')

	# User1 posts a tweet
	tweet1 = user1.post_tweet('Hello, world!')

	# User2 views trending tweets
	trending_tweets = Trending.get_trending_tweets()

	# User2 sends a direct message to User1
	message = user2.send_direct_message(user1, 'Hello!')

	# User2 follows User1
	user2.follow(user1)

	# User2 replies to User1's tweet
	reply = user2.reply_to_tweet(tweet1, 'Hello, user1!')

	# User2 mentions User1 in a tweet
	mention = user2.mention(user1, 'Check this out, @user1!')

