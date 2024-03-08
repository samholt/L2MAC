from models import Post

# Mock database
posts_db = {}


def create_post(user_id, text, image=None):
	if len(text) > 280:
		raise ValueError('Post is too long.')
	post = Post(len(posts_db) + 1, user_id, text, image)
	posts_db[post.id] = post
	return post


def delete_post(post_id):
	post = posts_db.get(post_id)
	if post:
		del posts_db[post_id]
		return 'Post deleted.'
	else:
		return 'Post not found.'


def like_post(post_id):
	post = posts_db.get(post_id)
	if post:
		post.likes += 1
		return post
	else:
		return 'Post not found.'


def retweet_post(post_id):
	post = posts_db.get(post_id)
	if post:
		post.retweets += 1
		return post
	else:
		return 'Post not found.'


def reply_to_post(post_id, user_id, text):
	if len(text) > 280:
		raise ValueError('Reply is too long.')
	reply = Post(len(posts_db) + 1, user_id, text)
	reply.reply_to = post_id
	posts_db[reply.id] = reply
	return reply if post_id in posts_db else None


def search_posts(keyword):
	return sorted([post for post in posts_db.values() if keyword.lower() in post.text.lower()], key=lambda post: post.id)


def filter_posts_by_hashtag(hashtag):
	return sorted([post for post in posts_db.values() if f'#{hashtag.lower()}' in post.text.lower()], key=lambda post: post.id)


def filter_posts_by_user_mention(username):
	return sorted([post for post in posts_db.values() if f'@{username.lower()}' in post.text.lower()], key=lambda post: post.id)
