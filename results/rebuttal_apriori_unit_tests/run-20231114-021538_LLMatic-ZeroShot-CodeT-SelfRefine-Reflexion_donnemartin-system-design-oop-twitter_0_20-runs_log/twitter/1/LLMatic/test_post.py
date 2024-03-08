import pytest
from post import create_post, posts_db

def test_create_post():
	user_id = 1
	content = 'This is a test post'
	assert create_post(user_id, content) == True


def test_like_post():
	user_id = 1
	content = 'This is a test post'
	create_post(user_id, content)
	post = posts_db[1]
	post.like_post()
	assert post.likes == 1


def test_retweet_post():
	user_id = 1
	content = 'This is a test post'
	create_post(user_id, content)
	post = posts_db[1]
	post.retweet_post()
	assert post.retweets == 1


def test_reply_to_post():
	user_id = 1
	content = 'This is a test post'
	create_post(user_id, content)
	post = posts_db[1]
	reply_content = 'This is a reply'
	post.reply_to_post(user_id, reply_content)
	assert len(post.replies) == 1
	assert post.replies[0].content == reply_content
