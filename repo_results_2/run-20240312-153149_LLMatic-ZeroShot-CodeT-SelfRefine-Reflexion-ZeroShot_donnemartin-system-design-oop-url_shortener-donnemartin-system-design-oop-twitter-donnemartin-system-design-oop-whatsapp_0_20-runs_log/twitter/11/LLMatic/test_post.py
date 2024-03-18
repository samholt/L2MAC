import datetime
import post


def test_create_post():
	new_post = post.Post('test_user', 'test_text', 'test_image')
	created_post = new_post.create()
	assert created_post['user'] == 'test_user'
	assert created_post['text'] == 'test_text'
	assert created_post['image'] == 'test_image'
	assert isinstance(created_post['timestamp'], datetime.datetime)
	assert created_post['likes'] == 0
	assert created_post['retweets'] == 0
	assert created_post['replies'] == []


def test_delete_post():
	new_post = post.Post('test_user', 'test_text', 'test_image')
	assert new_post.delete() == True
	assert new_post.user == None
	assert new_post.text == None
	assert new_post.image == None
	assert new_post.timestamp == None
	assert new_post.likes == None
	assert new_post.retweets == None
	assert new_post.replies == None


def test_like_post():
	new_post = post.Post('test_user', 'test_text', 'test_image')
	assert new_post.like() == 1


def test_retweet_post():
	new_post = post.Post('test_user', 'test_text', 'test_image')
	assert new_post.retweet() == 1


def test_reply_post():
	new_post = post.Post('test_user', 'test_text', 'test_image')
	reply = new_post.reply('reply_user', 'reply_text')
	assert len(reply) == 1
	assert reply[0]['user'] == 'reply_user'
	assert reply[0]['text'] == 'reply_text'
	assert isinstance(reply[0]['timestamp'], datetime.datetime)
	assert reply[0]['likes'] == 0
	assert reply[0]['retweets'] == 0
	assert reply[0]['replies'] == []
