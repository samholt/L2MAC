import pytest
from post import Post


def test_post_creation():
	post = Post('author', 'content', ['image1', 'image2'])
	assert post.author == 'author'
	assert post.content == 'content'
	assert post.images == ['image1', 'image2']
	assert post.likes == 0
	assert post.retweets == 0
	assert post.replies == []


def test_like():
	post = Post('author', 'content', ['image1', 'image2'])
	post.like()
	assert post.likes == 1


def test_retweet():
	post = Post('author', 'content', ['image1', 'image2'])
	post.retweet()
	assert post.retweets == 1


def test_reply():
	post = Post('author', 'content', ['image1', 'image2'])
	post.reply('reply')
	assert post.replies == ['reply']


def test_delete():
	post = Post('author', 'content', ['image1', 'image2'])
	post.delete()
	assert post.content == ''
	assert post.images == []
	assert post.likes == 0
	assert post.retweets == 0
	assert post.replies == []


def test_search():
	post1 = Post('author1', 'content1', ['image1', 'image2'])
	post2 = Post('author2', 'content2', ['image3', 'image4'])
	result = Post.search([post1, post2], 'content1')
	assert result == [post1]
