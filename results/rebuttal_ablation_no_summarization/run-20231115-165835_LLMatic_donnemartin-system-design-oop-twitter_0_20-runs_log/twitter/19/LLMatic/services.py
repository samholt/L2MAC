from models import User, Post

users_db = {}
posts_db = {}


def register_user(email, username, password):
	if email in users_db:
		return False
	user = User(email, username, password)
	users_db[email] = user
	return True

def authenticate_user(email, password):
	if email not in users_db:
		return False
	user = users_db[email]
	return user.authenticate(password)

def edit_profile(email, profile_picture, bio, website_link, location):
	if email not in users_db:
		return False
	user = users_db[email]
	user.profile_picture = profile_picture
	user.bio = bio
	user.website_link = website_link
	user.location = location
	return True

def toggle_privacy(email):
	if email not in users_db:
		return False
	user = users_db[email]
	user.is_private = not user.is_private
	return True

def create_post(user_email, text_content, images):
	if user_email not in users_db:
		return False
	user = users_db[user_email]
	post = Post(user, text_content, images)
	posts_db[len(posts_db)] = post
	return True

def delete_post(post_id):
	if post_id not in posts_db:
		return False
	del posts_db[post_id]
	return True

def search_posts(query):
	return [post for post in posts_db.values() if query in post.text_content]
