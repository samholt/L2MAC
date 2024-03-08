# This file will contain utility functions

from models import users_db, posts_db

def search_users(keyword):
	results = []
	for user in users_db.values():
		if keyword.lower() in user.username.lower():
			results.append(user)
	return results

def search_posts(keyword):
	results = []
	for post in posts_db.values():
		if keyword.lower() in post.content.lower():
			results.append(post)
	return results
