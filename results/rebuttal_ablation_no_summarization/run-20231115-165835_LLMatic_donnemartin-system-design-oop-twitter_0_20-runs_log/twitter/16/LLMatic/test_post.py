import datetime
from post import Post


def test_create_post():
	post = Post()
	user = 'test_user'
	text = 'test_text'
	image = 'test_image'
	new_post = post.create(user, text, image)
	assert new_post['user'] == user
	assert new_post['text'] == text
	assert new_post['image'] == image
	assert new_post['likes'] == 0
	assert new_post['retweets'] == 0
	assert new_post['replies'] == []


def test_delete_post():
	post = Post()
	user = 'test_user'
	text = 'test_text'
	image = 'test_image'
	new_post = post.create(user, text, image)
	timestamp = new_post['timestamp']
	assert post.delete(timestamp) == True
	assert post.delete(timestamp) == False


def test_like_post():
	post = Post()
	user = 'test_user'
	text = 'test_text'
	image = 'test_image'
	new_post = post.create(user, text, image)
	timestamp = new_post['timestamp']
	assert post.like(timestamp) == True
	assert new_post['likes'] == 1


def test_retweet_post():
	post = Post()
	user = 'test_user'
	text = 'test_text'
	image = 'test_image'
	new_post = post.create(user, text, image)
	timestamp = new_post['timestamp']
	assert post.retweet(timestamp) == True
	assert new_post['retweets'] == 1


def test_reply_post():
	post = Post()
	user = 'test_user'
	text = 'test_text'
	image = 'test_image'
	new_post = post.create(user, text, image)
	timestamp = new_post['timestamp']
	reply = 'test_reply'
	assert post.reply(timestamp, reply) == True
	assert new_post['replies'] == [reply]
