import pytest
from posts import create_post, search_posts, filter_posts_by_hashtag, filter_posts_by_user_mention


def test_search_posts():
	create_post(1, 'This is a test post.')
	create_post(2, 'Another test post.')
	create_post(3, 'Test post three.')
	results = search_posts('test')
	assert len(results) == 3
	assert 'test' in results[0].text.lower()
	assert 'test' in results[1].text.lower()
	assert 'test' in results[2].text.lower()


def test_filter_posts_by_hashtag():
	create_post(1, 'This is a #test post.')
	create_post(2, 'Another #test post.')
	create_post(3, 'Post without hashtag.')
	results = filter_posts_by_hashtag('test')
	assert len(results) == 2
	assert '#test' in results[0].text.lower()
	assert '#test' in results[1].text.lower()


def test_filter_posts_by_user_mention():
	create_post(1, 'This is a post mentioning @user1.')
	create_post(2, 'Another post mentioning @user1.')
	create_post(3, 'Post without mention.')
	results = filter_posts_by_user_mention('user1')
	assert len(results) == 2
	assert '@user1' in results[0].text.lower()
	assert '@user1' in results[1].text.lower()
