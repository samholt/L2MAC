import pytest
from post import Post


def test_search():
	posts = [Post('Hello world'), Post('Goodbye world'), Post('Hello again')]
	assert Post.search(posts, 'Hello') == [posts[0], posts[2]]
	assert Post.search(posts, 'world') == [posts[0], posts[1]]
	assert Post.search(posts, 'Goodbye') == [posts[1]]
	assert Post.search(posts, 'again') == [posts[2]]
