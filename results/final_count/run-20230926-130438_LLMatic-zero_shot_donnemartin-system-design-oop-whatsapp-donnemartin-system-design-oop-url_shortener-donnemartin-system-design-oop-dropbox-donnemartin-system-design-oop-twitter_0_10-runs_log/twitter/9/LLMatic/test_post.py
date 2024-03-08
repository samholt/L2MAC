import pytest
from post import Post

def test_create_post():
	text = 'This is a test post'
	images = ['image1.jpg', 'image2.jpg']
	user = 'test_user'
	post = Post.create_post(text, images, user)
	assert post.text == text
	assert post.images == images
	assert post.user == user

def test_delete_post():
	text = 'This is a test post'
	images = ['image1.jpg', 'image2.jpg']
	user = 'test_user'
	post = Post.create_post(text, images, user)
	Post.delete_post(post)
	assert post.text == None
	assert post.images == None
	assert post.user == None

def test_like_post():
	post = Post('Test post', [], 'test_user')
	post.like_post()
	assert post.likes == 1

def test_retweet_post():
	post = Post('Test post', [], 'test_user')
	post.retweet_post()
	assert post.retweets == 1

def test_reply_to_post():
	post = Post('Test post', [], 'test_user')
	reply = 'This is a reply'
	post.reply_to_post(reply)
	assert post.replies == [reply]

def test_search_posts():
	posts = [Post('Test post', [], 'test_user'), Post('Another test post', [], 'another_test_user')]
	search_results = Post.search_posts(posts, 'Another')
	assert len(search_results) == 1
	assert search_results[0].text == 'Another test post'

def test_filter_posts():
	posts = [Post('Test post #hashtag', [], 'test_user'), Post('Another test post', [], 'another_test_user')]
	filtered_posts = Post.filter_posts(posts, '#hashtag')
	assert len(filtered_posts) == 1
	assert filtered_posts[0].text == 'Test post #hashtag'
