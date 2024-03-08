import pytest
from post import Post


def test_create_post():
	user = 'test_user'
	text = 'test_text'
	image = 'test_image.jpg'
	post = Post.create_post(user, text, image)
	assert post.user == user
	assert post.text == text
	assert post.image == image


def test_delete_post():
	user = 'test_user'
	text = 'test_text'
	image = 'test_image.jpg'
	post = Post.create_post(user, text, image)
	post.delete_post()
	assert post.user is None
	assert post.text is None
	assert post.image is None
	assert post.timestamp is None


def test_like_unlike_post():
	post = Post('test_user', 'test_text')
	post.like_post()
	assert post.likes == 1
	post.unlike_post()
	assert post.likes == 0


def test_retweet():
	post = Post('test_user', 'test_text')
	post.retweet()
	assert post.retweets == 1


def test_reply():
	post = Post('test_user', 'test_text')
	reply = 'test_reply'
	post.reply(reply)
	assert post.replies == [reply]


def test_view_replies():
	post = Post('test_user', 'test_text')
	reply1 = 'test_reply1'
	reply2 = 'test_reply2'
	post.reply(reply1)
	post.reply(reply2)
	assert post.view_replies() == [reply1, reply2]
