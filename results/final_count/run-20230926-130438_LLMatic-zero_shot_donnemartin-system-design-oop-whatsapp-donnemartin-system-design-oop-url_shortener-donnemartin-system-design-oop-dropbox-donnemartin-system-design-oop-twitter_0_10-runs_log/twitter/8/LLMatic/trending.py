import re
from collections import Counter

# Mock database
posts_db = []
users_db = {}


def add_post_to_db(post):
	posts_db.append(post)


def add_user_to_db(user):
	users_db[user['username']] = user


def get_trending_hashtags():
	# Extract hashtags from all posts
	hashtags = [re.findall(r'#\w+', post['text']) for post in posts_db]
	hashtags = [hashtag for sublist in hashtags for hashtag in sublist]

	# Count occurrences of each hashtag
	hashtag_counts = Counter(hashtags)

	# Get the 10 most common hashtags
	trending_hashtags = hashtag_counts.most_common(10)

	return trending_hashtags


def recommend_users(user):
	# Get all users that the given user is not already following
	not_following = [u for u in users_db.keys() if u not in users_db[user].get('following', [])]

	# Recommend the first 5 users that the given user is not already following
	recommended_users = not_following[:5]

	return recommended_users
