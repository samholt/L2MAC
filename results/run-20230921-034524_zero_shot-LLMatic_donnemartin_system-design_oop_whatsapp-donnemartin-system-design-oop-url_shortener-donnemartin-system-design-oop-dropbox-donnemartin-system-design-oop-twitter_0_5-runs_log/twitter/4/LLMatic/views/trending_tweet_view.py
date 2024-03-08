from controllers.trending_tweet_controller import TrendingTweetController


class TrendingTweetView:
	def __init__(self, controller: TrendingTweetController):
		self.controller = controller

	def display_trending_tweets(self):
		trending_tweets = self.controller.get_trending_tweets()
		for trending_tweet in trending_tweets:
			print(f'Tweet: {trending_tweet.tweet.content}, Popularity: {trending_tweet.popularity}')
