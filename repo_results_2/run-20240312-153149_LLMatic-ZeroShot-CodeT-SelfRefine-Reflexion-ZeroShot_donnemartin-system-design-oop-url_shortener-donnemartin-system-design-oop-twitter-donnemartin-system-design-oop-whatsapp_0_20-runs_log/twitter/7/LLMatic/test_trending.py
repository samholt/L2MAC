import pytest
from trending import Trending
from post import Post


def test_filter():
	posts = [Post('Hello world', hashtags=['#hello']), Post('Goodbye world', topics=['goodbye']), Post('Hello again', hashtags=['#hello'], topics=['again'])]
	assert Trending.filter(posts, '#hello') == [posts[0], posts[2]]
	assert Trending.filter(posts, 'goodbye') == [posts[1]]
	assert Trending.filter(posts, 'again') == [posts[2]]
