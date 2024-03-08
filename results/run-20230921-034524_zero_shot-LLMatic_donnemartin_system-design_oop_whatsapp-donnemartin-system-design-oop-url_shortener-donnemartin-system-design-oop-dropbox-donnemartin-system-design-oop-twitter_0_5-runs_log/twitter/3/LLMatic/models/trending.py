class Trending:
	def __init__(self):
		self.tweets = []

	def calculate_trending(self):
		# Calculate trending tweets based on the number of likes and retweets
		self.tweets.sort(key=lambda tweet: (tweet.likes, tweet.retweets), reverse=True)

	def display_trending(self):
		# Display the top 10 trending tweets
		for tweet in self.tweets[:10]:
			print(f"{tweet.user.username}: {tweet.text} (Likes: {tweet.likes}, Retweets: {tweet.retweets})")
