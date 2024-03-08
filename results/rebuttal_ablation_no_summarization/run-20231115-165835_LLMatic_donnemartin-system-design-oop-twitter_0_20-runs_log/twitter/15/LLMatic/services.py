import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Post
from collections import Counter
from datetime import datetime, timedelta

SECRET_KEY = 'secret'


def register_user(email, username, password):
	user = User(id=None, email=email, username=username, password=password, profile_picture=None, bio=None, website_link=None, location=None)
	# TODO: Save user to database
	return user


def authenticate_user(email, password):
	# TODO: Retrieve user from database
	user = User(id=None, email=email, username=None, password=password, profile_picture=None, bio=None, website_link=None, location=None)
	if user and user.check_password(password):
		token = jwt.encode({'email': user.email}, SECRET_KEY, algorithm='HS256')
		return token
	return None


def update_profile(user_id, profile_picture=None, bio=None, website_link=None, location=None, is_private=False):
	# TODO: Retrieve user from database using user_id
	user = User(id=user_id, email=None, username=None, password=None, profile_picture=profile_picture, bio=bio, website_link=website_link, location=location)
	user.is_private = is_private
	# TODO: Save updated user to database
	return user


def create_post(user_id, text, image=None):
	if len(text) > 280:
		return 'Post is too long'
	post = Post(id=None, user_id=user_id, text=text, image=image)
	# TODO: Save post to database
	return post


def like_post(post_id):
	# TODO: Retrieve post from database using post_id
	post = Post(id=post_id, user_id=None, text=None, image=None)
	post.like()
	# TODO: Save updated post to database
	return post


def retweet_post(post_id):
	# TODO: Retrieve post from database using post_id
	post = Post(id=post_id, user_id=None, text=None, image=None)
	post.retweet()
	# TODO: Save updated post to database
	return post


def reply_to_post(post_id, reply):
	# TODO: Retrieve post from database using post_id
	post = Post(id=post_id, user_id=None, text=None, image=None)
	post.reply(reply)
	# TODO: Save updated post to database
	return post


def search(keyword):
	# TODO: Implement search functionality
	pass


def follow_user(follower_id, followee_id):
	# TODO: Retrieve users from database using follower_id and followee_id
	follower = User(id=follower_id, email=None, username=None, password=None, profile_picture=None, bio=None, website_link=None, location=None)
	followee = User(id=followee_id, email=None, username=None, password=None, profile_picture=None, bio=None, website_link=None, location=None)
	follower.follow(followee)
	# TODO: Save updated users to database
	return follower, followee


def unfollow_user(follower_id, followee_id):
	# TODO: Retrieve users from database using follower_id and followee_id
	follower = User(id=follower_id, email=None, username=None, password=None, profile_picture=None, bio=None, website_link=None, location=None)
	followee = User(id=followee_id, email=None, username=None, password=None, profile_picture=None, bio=None, website_link=None, location=None)
	follower.unfollow(followee)
	# TODO: Save updated users to database
	return follower, followee


def get_timeline(user_id):
	# TODO: Retrieve user from database using user_id
	user = User(id=user_id, email=None, username=None, password=None, profile_picture=None, bio=None, website_link=None, location=None)
	timeline = []
	for followee in user.following:
		timeline.extend(followee.posts)
	timeline.sort(key=lambda post: post.timestamp, reverse=True)
	return timeline


def get_notifications(user_id):
	# TODO: Retrieve user from database using user_id
	user = User(id=user_id, email=None, username=None, password=None, profile_picture=None, bio=None, website_link=None, location=None)
	new_followers = [follower for follower in user.followers if follower not in user.following]
	return new_followers


def get_trending_hashtags():
	# TODO: Retrieve all posts from database
	posts = []
	hashtags = [hashtag for post in posts for hashtag in post.hashtags]
	counts = Counter(hashtags)
	trending = counts.most_common(10)
	return trending


def get_recommended_users(user_id):
	# TODO: Retrieve user from database using user_id
	user = User(id=user_id, email=None, username=None, password=None, profile_picture=None, bio=None, website_link=None, location=None)
	# TODO: Retrieve all other users from database
	other_users = []
	recommendations = []
	for other_user in other_users:
		if other_user not in user.following and len(set(user.following) & set(other_user.following)) > 0:
			recommendations.append(other_user)
	recommendations.sort(key=lambda user: len(user.posts), reverse=True)
	return recommendations[:10]
