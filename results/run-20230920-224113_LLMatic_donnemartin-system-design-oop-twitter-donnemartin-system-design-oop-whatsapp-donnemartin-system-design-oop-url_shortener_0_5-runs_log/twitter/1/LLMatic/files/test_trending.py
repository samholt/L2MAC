import pytest
from trending import Trending


def test_calculate_trending_tweets():
	trending = Trending()
	trending.calculate_trending_tweets()
	# Since the method is not implemented, we can't assert anything


def test_display_trending_tweets():
	trending = Trending()
	trending.display_trending_tweets()
	# Since the method is not implemented, we can't assert anything
