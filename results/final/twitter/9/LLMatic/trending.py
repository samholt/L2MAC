from collections import Counter
from models import users_db, posts_db


def get_trending_hashtags(global_trending=True, location=None):
	all_hashtags = [hashtag for post in posts_db.values() for hashtag in post.hashtags]
	trending_hashtags = Counter(all_hashtags).most_common(10)
	return trending_hashtags


def recommend_users(user_id):
	user = users_db[user_id]
	all_users = [u for u in users_db.values() if u.id != user_id and u not in user.blocked]
	recommended_users = sorted(all_users, key=lambda u: len(set(user.interests).intersection(set(u.interests))) + len(set(user.following).intersection(set(u.followers))) + u.activity_level, reverse=True)[:10]
	return recommended_users
