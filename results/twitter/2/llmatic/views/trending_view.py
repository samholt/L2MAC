from models.trending import Trending


class TrendingView:
	@staticmethod
	def display_trending(trending: Trending):
		for tweet in trending.get_trending_tweets():
			print(f'Trending: {tweet.user.username}: {tweet.content}')
