from trending import Trending


def test_get_trending_topics():
	trending = Trending()
	trending.add_topic('Python')
	trending.add_topic('Python')
	trending.add_topic('JavaScript')
	assert trending.get_trending_topics() == [('Python', 2), ('JavaScript', 1)]


def test_sort_trending_topics():
	trending = Trending()
	trending.add_topic('Python', 'USA')
	trending.add_topic('Python', 'USA')
	trending.add_topic('JavaScript', 'USA')
	trending.add_topic('Java', 'India')
	assert trending.sort_trending_topics('USA') == [('USA Python', 2), ('USA JavaScript', 1)]
	assert trending.sort_trending_topics('India') == [('India Java', 1)]
	assert trending.sort_trending_topics() == [('USA Python', 2), ('USA JavaScript', 1), ('India Java', 1)]
