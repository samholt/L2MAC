from models.user import User
from models.tweet import Tweet
from models.conversation import Conversation
from models.direct_message import DirectMessage
from models.trending import Trending

# Create users
user1 = User('user1', 'password1')
user2 = User('user2', 'password2')

# User1 posts a tweet
tweet1 = Tweet('Hello, world!', user1)
user1.post_tweet(tweet1)

# User2 replies to the tweet
reply1 = Tweet('Hello, user1!', user2)
user2.reply_to_tweet(tweet1, reply1)

# User1 sends a direct message to User2
user1.send_direct_message(user2, 'Hello, user2!')

# User1 follows User2
user1.follow_user(user2)

# Create a conversation and add the tweets to it
conversation = Conversation()
conversation.add_tweet(tweet1)
conversation.add_tweet(reply1)

# Create trending and calculate trending tweets
trending = Trending()
trending.calculate_trending()
trending.display_trending()

