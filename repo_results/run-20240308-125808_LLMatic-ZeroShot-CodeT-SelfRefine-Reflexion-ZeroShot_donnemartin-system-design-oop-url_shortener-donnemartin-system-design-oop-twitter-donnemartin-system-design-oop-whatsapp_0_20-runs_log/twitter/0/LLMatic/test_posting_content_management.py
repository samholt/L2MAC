import pytest
from posting_content_management import PostingContentManagement, Post
from user_management import User


def test_like_post():
	content_management = PostingContentManagement()
	user = User('email', 'username', 'password')
	post = Post(user, 'Hello!', [])
	content_management.posts.append(post)
	user.like(post)
	assert post.likes == 1


def test_retweet_post():
	content_management = PostingContentManagement()
	user = User('email', 'username', 'password')
	post = Post(user, 'Hello!', [])
	content_management.posts.append(post)
	user.retweet(post)
	assert post.retweets == 1


def test_reply_post():
	content_management = PostingContentManagement()
	user = User('email', 'username', 'password')
	post = Post(user, 'Hello!', [])
	content_management.posts.append(post)
	user.reply(post, 'Reply!')
	assert len(post.replies) == 1
