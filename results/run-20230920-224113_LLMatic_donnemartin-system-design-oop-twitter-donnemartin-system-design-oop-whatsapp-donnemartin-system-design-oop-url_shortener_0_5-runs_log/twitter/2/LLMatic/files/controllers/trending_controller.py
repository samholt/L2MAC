from models.trending import Trending
from views.trending_view import TrendingView


class TrendingController:
	@staticmethod
	def get_trending_tweets(trending):
		trending_tweets = trending.get_trending_tweets()
		TrendingView.display_trending(trending)
		return trending_tweets
