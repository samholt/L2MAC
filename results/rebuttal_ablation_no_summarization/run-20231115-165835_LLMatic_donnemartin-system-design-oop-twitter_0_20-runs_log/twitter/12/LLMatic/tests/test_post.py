import pytest
from post import Post


def test_search_posts():
	Post.create_post('user1', 'This is a test post', [])
	Post.create_post('user2', 'Another test post', [])
	Post.create_post('user3', 'Yet another test post', [])
	results = Post.search_posts('test')
	assert len(results) == 3
	assert all('test' in post.text for post in results)


def test_filter_posts():
	Post.create_post('user1', 'This is a #test post', [])
	Post.create_post('user2', 'Another #test post', [])
	Post.create_post('user3', 'Yet another #test post', [])
	results = Post.filter_posts('hashtag', 'test')
	assert len(results) == 3
	assert all('#test' in post.text for post in results)

	Post.create_post('user1', 'This is a @test post', [])
	Post.create_post('user2', 'Another @test post', [])
	Post.create_post('user3', 'Yet another @test post', [])
	results = Post.filter_posts('mention', 'test')
	assert len(results) == 3
	assert all('@test' in post.text for post in results)

	Post.create_post('user1', 'This is a trending post', [])
	Post.create_post('user2', 'Another trending post', [])
	Post.create_post('user3', 'Yet another trending post', [])
	results = Post.filter_posts('trending', ['trending'])
	assert len(results) == 3
	assert all('trending' in post.text for post in results)


def test_get_trending_topics():
	Post.posts_db.clear()
	Post.create_post('user1', 'This is a #trending post', [])
	Post.create_post('user2', 'Another #trending post', [])
	Post.create_post('user3', 'Yet another #trending post', [])
	trending_topics = Post.get_trending_topics()
	assert len(trending_topics) == 1
	assert trending_topics[0][0] == '#trending'
	assert trending_topics[0][1] == 3
