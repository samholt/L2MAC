import pytest
from post import Post


def test_create_post():
	post = Post('user1', 'Hello, World!')
	assert post.create_post() == {'user1': {'text': 'Hello, World!', 'images': None, 'likes': 0, 'retweets': 0, 'replies': [], 'location': 'global'}}


def test_delete_post():
	post = Post('user1', 'Hello, World!')
	post.create_post()
	assert post.delete_post() == 'Post deleted'


def test_like_post():
	post = Post('user1', 'Hello, World!')
	post.create_post()
	assert post.like_post() == 'Post liked'


def test_retweet_post():
	post = Post('user1', 'Hello, World!')
	post.create_post()
	assert post.retweet_post() == 'Post retweeted'


def test_reply_post():
	post = Post('user1', 'Hello, World!')
	post.create_post()
	assert post.reply_post('Nice post!') == 'Reply added'


def test_search_posts_by_keyword():
	post = Post('user1', 'Hello, World!')
	post.create_post()
	assert post.search_posts_by_keyword('World') == [{'text': 'Hello, World!', 'images': None, 'likes': 0, 'retweets': 0, 'replies': [], 'location': 'global'}]


def test_filter_posts_by_hashtag():
	post = Post('user1', 'Hello, #World!')
	post.create_post()
	assert post.filter_posts_by_hashtag('#World') == [{'text': 'Hello, #World!', 'images': None, 'likes': 0, 'retweets': 0, 'replies': [], 'location': 'global'}]


def test_filter_posts_by_user_mentions():
	post = Post('user1', 'Hello, @user2!')
	post.create_post()
	assert post.filter_posts_by_user_mentions('user2') == [{'text': 'Hello, @user2!', 'images': None, 'likes': 0, 'retweets': 0, 'replies': [], 'location': 'global'}]


def test_filter_posts_by_trending_topics():
	post = Post('user1', 'Hello, World! #trending')
	post.create_post()
	assert post.filter_posts_by_trending_topics('#trending') == [{'text': 'Hello, World! #trending', 'images': None, 'likes': 0, 'retweets': 0, 'replies': [], 'location': 'global'}]


def test_get_trending_topics():
	post1 = Post('user1', 'Hello, #World!')
	post1.create_post()
	post2 = Post('user2', 'Hello, #World!')
	post2.create_post()
	post3 = Post('user3', 'Hello, #Python!')
	post3.create_post()
	assert post1.get_trending_topics() == [('#World!', 2), ('#Python!', 1)]


def test_sort_trending_topics():
	post1 = Post('user1', 'Hello, #World!', location='USA')
	post1.create_post()
	post2 = Post('user2', 'Hello, #World!', location='USA')
	post2.create_post()
	post3 = Post('user3', 'Hello, #Python!', location='UK')
	post3.create_post()
	assert post1.sort_trending_topics('USA') == [('#World!', 2)]
	assert post3.sort_trending_topics('UK') == [('#Python!', 1)]
