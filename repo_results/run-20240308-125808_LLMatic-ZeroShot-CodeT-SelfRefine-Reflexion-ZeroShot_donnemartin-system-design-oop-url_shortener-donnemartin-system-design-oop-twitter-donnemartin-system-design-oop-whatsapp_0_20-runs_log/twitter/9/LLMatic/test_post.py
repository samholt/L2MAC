import post


def test_create_post():
	new_post = post.Post.create_post('user1', 'This is a test post')
	assert new_post.user_id == 'user1'
	assert new_post.text == 'This is a test post'
	assert new_post.image is None
	assert new_post.likes == 0
	assert new_post.retweets == 0
	assert new_post.replies == []


def test_delete_post():
	new_post = post.Post.create_post('user1', 'This is a test post')
	new_post.delete_post()
	assert new_post.user_id is None
	assert new_post.text is None
	assert new_post.image is None
	assert new_post.timestamp is None
	assert new_post.likes == 0
	assert new_post.retweets == 0
	assert new_post.replies == []


def test_like_post():
	new_post = post.Post.create_post('user1', 'This is a test post')
	new_post.like_post()
	assert new_post.likes == 1


def test_retweet_post():
	new_post = post.Post.create_post('user1', 'This is a test post')
	new_post.retweet_post()
	assert new_post.retweets == 1


def test_reply_to_post():
	new_post = post.Post.create_post('user1', 'This is a test post')
	reply = new_post.reply_to_post('user2', 'This is a reply')
	assert len(new_post.replies) == 1
	assert new_post.replies[0].user_id == 'user2'
	assert new_post.replies[0].text == 'This is a reply'
