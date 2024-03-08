import pytest
from trending import Trending


def test_trending():
	trending = Trending()

	# Add hashtags
	for _ in range(10):
		trending.add_hashtag('#test')
	for _ in range(5):
		trending.add_hashtag('#python')

	# Add mentions
	for _ in range(7):
		trending.add_mention('@user1')
	for _ in range(3):
		trending.add_mention('@user2')

	# Add locations
	for _ in range(6):
		trending.add_location('New York')
	for _ in range(4):
		trending.add_location('San Francisco')

	assert trending.get_trending_hashtags() == [('#test', 10), ('#python', 5)]
	assert trending.get_trending_mentions() == [('@user1', 7), ('@user2', 3)]
	assert trending.get_trending_locations() == [('New York', 6), ('San Francisco', 4)]
