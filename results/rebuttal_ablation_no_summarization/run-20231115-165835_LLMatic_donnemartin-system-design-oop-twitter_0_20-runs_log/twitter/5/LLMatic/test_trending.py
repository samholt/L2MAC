import pytest
from trending import Trending
from post import Post


def test_trending_topics():
	user = 'test_user'
	posts = [
		Post(user, 'Hello #world'),
		Post(user, 'Another post with #world'),
		Post(user, 'This is a #test'),
		Post(user, '#world is great'),
		Post(user, 'I love #coding'),
		Post(user, '#coding #world')
	]
	trending = Trending(posts)
	assert trending.get_trending_topics() == [('#world', 4), ('#coding', 2), ('#test', 1)]
