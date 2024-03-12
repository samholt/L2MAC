import pytest
from trending import Trending

def test_trending():
	trending = Trending()
	trending.add_topic('#AI', 'global')
	trending.add_topic('#ML', 'USA')
	trending.add_topic('#AI', 'global')
	assert trending.get_trending_topics() == [('#AI', {'count': 2, 'location': 'global'}), ('#ML', {'count': 1, 'location': 'USA'})]
	assert trending.sort_trending_topics() == [('#AI', {'count': 2, 'location': 'global'}), ('#ML', {'count': 1, 'location': 'USA'})]
	assert trending.sort_trending_topics('USA') == [('#ML', {'count': 1, 'location': 'USA'})]
