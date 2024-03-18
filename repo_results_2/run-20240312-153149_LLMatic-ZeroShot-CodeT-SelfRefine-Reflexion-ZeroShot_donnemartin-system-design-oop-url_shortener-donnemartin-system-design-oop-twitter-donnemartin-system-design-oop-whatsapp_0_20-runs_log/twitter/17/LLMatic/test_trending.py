import pytest
from trending import Trending

def test_get_trending_topics():
	trending = Trending()
	trending.trending_topics = {'#topic1': 100, '#topic2': 50, '#topic3': 150}
	assert trending.get_trending_topics() == [('#topic3', 150), ('#topic1', 100), ('#topic2', 50)]

def test_sort_trending_topics():
	trending = Trending()
	trending.trending_topics = {'US#topic1': 100, 'US#topic2': 50, 'UK#topic1': 150, 'UK#topic2': 200}
	assert trending.sort_trending_topics('US') == [('US#topic1', 100), ('US#topic2', 50)]
	assert trending.sort_trending_topics('UK') == [('UK#topic2', 200), ('UK#topic1', 150)]
	assert trending.sort_trending_topics() == [('UK#topic2', 200), ('UK#topic1', 150), ('US#topic1', 100), ('US#topic2', 50)]

