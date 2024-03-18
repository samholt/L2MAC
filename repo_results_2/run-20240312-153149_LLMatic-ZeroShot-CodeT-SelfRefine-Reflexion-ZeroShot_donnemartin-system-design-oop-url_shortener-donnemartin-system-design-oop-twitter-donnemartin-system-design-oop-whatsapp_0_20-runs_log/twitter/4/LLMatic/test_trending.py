import pytest
from trending import Trending

def test_get_trending_topics():
	trending = Trending()
	trending.trending_topics = {'#topic1': 100, '#topic2': 200, '#topic3': 150}
	assert trending.get_trending_topics() == [('#topic2', 200), ('#topic3', 150), ('#topic1', 100)]

def test_sort_trending_topics():
	trending = Trending()
	trending.trending_topics = {'US#topic1': 100, 'US#topic2': 200, 'UK#topic1': 150, 'UK#topic2': 250}
	assert trending.sort_trending_topics('US') == [('US#topic2', 200), ('US#topic1', 100)]
	assert trending.sort_trending_topics() == [('UK#topic2', 250), ('US#topic2', 200), ('UK#topic1', 150), ('US#topic1', 100)]

