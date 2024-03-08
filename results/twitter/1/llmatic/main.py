from user import User
from tweet import Tweet
from direct_message import DirectMessage
from trending import Trending


if __name__ == '__main__':
	# Create some users
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')

	# Users post some tweets
	user1.post_tweet(Tweet(user1, 'Hello, world!'))
	user2.post_tweet(Tweet(user2, 'Hello, user1!'))

	# Users send some direct messages
	user1.send_direct_message(user2, 'Hello, user2!')
	user2.send_direct_message(user1, 'Hello, user1!')

	# Users follow each other
	user1.follow_user(user2)
	user2.follow_user(user1)

	# Display trending tweets
	trending = Trending()
	trending.display_trending_tweets()
