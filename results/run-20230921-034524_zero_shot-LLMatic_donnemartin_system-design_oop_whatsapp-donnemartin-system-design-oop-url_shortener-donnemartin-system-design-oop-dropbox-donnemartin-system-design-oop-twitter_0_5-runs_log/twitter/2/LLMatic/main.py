from user import User
from tweet import Tweet
from direct_message import DirectMessage
from conversation import Conversation
from trending import Trending


def main():
	# Create some users
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')

	# User1 posts a tweet
	tweet1 = Tweet(user1, 'Hello, world!', 'public')
	user1.post_tweet(tweet1)

	# User2 replies to the tweet
	reply1 = Tweet(user2, 'Hello, user1!', 'public')
	user2.reply_to_tweet(tweet1, reply1)

	# User1 views trending tweets
	trending = Trending([tweet1, reply1])
	user1.view_trending_tweets(trending)

	# User1 sends a direct message to user2
	dm = DirectMessage(user1, user2, 'Hello, user2!')
	user1.send_direct_message(dm)

	# User1 mentions user2 in a tweet
	mention_tweet = Tweet(user1, 'Hello, @user2!', 'public')
	user1.mention_user(user2, mention_tweet)

	# User1 follows user2
	user1.follow_user(user2)


if __name__ == '__main__':
	main()
