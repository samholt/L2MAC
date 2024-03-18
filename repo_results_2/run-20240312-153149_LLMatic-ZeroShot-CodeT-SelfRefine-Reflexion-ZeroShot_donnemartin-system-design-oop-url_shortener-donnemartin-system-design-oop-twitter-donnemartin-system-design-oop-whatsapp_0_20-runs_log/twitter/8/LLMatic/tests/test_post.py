import pytest
from post import Post
from user import User
from comment import Comment

def test_post_interaction():
	user = User('testuser', 'testuser@example.com', 'password')
	post = Post('This is a test post', [], user)
	comment = Comment('This is a test comment', user, post)

	post.like_post()
	post.retweet_post()
	post.reply_to_post(comment)

	assert post.likes == 1
	assert post.retweets == 1
	assert len(post.comments) == 1
	assert post.comments[0]['text'] == 'This is a test comment'
	assert post.comments[0]['user'] == 'testuser'
	assert post.comments[0]['post'] == 'This is a test post'
