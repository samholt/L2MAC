import post


def test_create_post():
	post_dict = {}
	post1 = post.Post.create_post('user1', 'Hello World')
	post_dict[1] = post1
	assert post1 in post_dict.values()


def test_delete_post():
	post_dict = {}
	post1 = post.Post.create_post('user1', 'Hello World')
	post_dict[1] = post1
	assert post.Post.delete_post(post_dict, 1) is True
	assert post1 not in post_dict.values()


def test_like_post():
	post1 = post.Post.create_post('user1', 'Hello World')
	post1.like_post()
	assert post1.likes == 1


def test_retweet_post():
	post1 = post.Post.create_post('user1', 'Hello World')
	post1.retweet_post()
	assert post1.retweets == 1


def test_reply_to_post():
	post1 = post.Post.create_post('user1', 'Hello World')
	reply = post1.reply_to_post('user2', 'Hello back')
	assert reply in post1.replies
