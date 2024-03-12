import pytest
from trending import Trending

def test_trending():
	trending = Trending()
	trending.add_topic('#python', 'global')
	trending.add_topic('#ai', 'global')
	trending.add_topic('#python', 'global')
	trending.add_topic('#ai', 'USA')
	assert trending.get_trending_topics() == [('#python', {'count': 2, 'locations': ['global', 'global']}), ('#ai', {'count': 2, 'locations': ['global', 'USA']})]
	assert trending.get_trending_topics('USA') == [('#ai', {'count': 2, 'locations': ['global', 'USA']})]
