import post


def test_create_post():
	new_post = post.Post('test_user', 'test_content', 'test_image')
	assert new_post.create() == {'user': 'test_user', 'content': 'test_content', 'image': 'test_image', 'timestamp': new_post.timestamp, 'likes': 0, 'retweets': 0, 'replies': []}


def test_delete_post():
	new_post = post.Post('test_user', 'test_content', 'test_image')
	assert new_post.delete() == True
	assert new_post.user == None
	assert new_post.content == None
	assert new_post.image == None
	assert new_post.timestamp == None
	assert new_post.likes == None
	assert new_post.retweets == None
	assert new_post.replies == None


def test_like_post():
	new_post = post.Post('test_user', 'test_content', 'test_image')
	assert new_post.like() == 1


def test_retweet_post():
	new_post = post.Post('test_user', 'test_content', 'test_image')
	assert new_post.retweet() == 1


def test_reply_post():
	new_post = post.Post('test_user', 'test_content', 'test_image')
	reply_content = 'test_reply'
	assert new_post.reply(reply_content) == [{'user': 'test_user', 'content': 'test_reply', 'image': None, 'timestamp': new_post.replies[0]['timestamp'], 'likes': 0, 'retweets': 0, 'replies': []}]

