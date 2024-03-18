from user import users_db
from post import post_db

def search(keyword):
	result = {'users': [], 'posts': []}

	# Search in users
	for username, user in users_db.items():
		if keyword in username or (user.bio and keyword in user.bio):
			result['users'].append(username)

	# Search in posts
	for user, posts in post_db.items():
		for post in posts:
			if keyword in post.text:
				result['posts'].append(post)

	return result

def search_user(keyword):
	for username, user in users_db.items():
		if keyword in username:
			return user
	return 'User not found'

def search_post(keyword):
	for user, posts in post_db.items():
		for post in posts:
			if keyword in post.text:
				return post
	return 'Post not found'
