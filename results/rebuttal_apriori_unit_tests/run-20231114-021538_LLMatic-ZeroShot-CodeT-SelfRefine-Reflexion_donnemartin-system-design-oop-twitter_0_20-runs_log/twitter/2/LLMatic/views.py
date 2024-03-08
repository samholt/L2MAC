import jwt
from models import User, Post


mock_db = {}
mock_posts_db = {}


def register_user(username, email, password, profile_picture=None, bio=None, website=None, location=None):
	user_id = len(mock_db) + 1
	user = User(user_id, username, email, password, profile_picture, bio, website, location)
	mock_db[user_id] = user
	return True


def authenticate_user(email, password):
	for user in mock_db.values():
		if user.email == email and user.password == User.hash_password(password):
			token = jwt.encode({'user_id': user.id}, 'secret', algorithm='HS256')
			return token
	return False


def get_user_profile(user_id):
	return mock_db.get(user_id, None)


def update_user_profile(token, profile_picture=None, bio=None, website=None, location=None):
	try:
		decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
		user_id = decoded['user_id']
		user = mock_db.get(user_id, None)
		if user:
			user.profile_picture = profile_picture or user.profile_picture
			user.bio = bio or user.bio
			user.website = website or user.website
			user.location = location or user.location
			return True
	except:
		return False


def create_post(token, content):
	try:
		decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
		user_id = decoded['user_id']
		post_id = len(mock_posts_db) + 1
		post = Post(post_id, user_id, content)
		mock_posts_db[post_id] = post
		return post_id
	except:
		return False


def delete_post(token, post_id):
	try:
		decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
		user_id = decoded['user_id']
		post = mock_posts_db.get(post_id, None)
		if post and post.user_id == user_id:
			del mock_posts_db[post_id]
			return True
		return False
	except:
		return False


def get_post(post_id):
	return mock_posts_db.get(post_id, None)


def like_post(token, post_id):
	try:
		decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
		user_id = decoded['user_id']
		post = mock_posts_db.get(post_id, None)
		if post:
			post.likes += 1
			return True
		return False
	except:
		return False


def retweet_post(token, post_id):
	try:
		decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
		user_id = decoded['user_id']
		post = mock_posts_db.get(post_id, None)
		if post:
			post.retweets += 1
			return True
		return False
	except:
		return False


def reply_to_post(token, post_id, reply_content):
	try:
		decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
		user_id = decoded['user_id']
		post = mock_posts_db.get(post_id, None)
		if post:
			post.replies.append(reply_content)
			return True
		return False
	except:
		return False


def search_posts(keyword):
	results = [post for post in mock_posts_db.values() if keyword in post.content]
	return results


def search_users(keyword):
	results = [user for user in mock_db.values() if keyword in user.username]
	return results

