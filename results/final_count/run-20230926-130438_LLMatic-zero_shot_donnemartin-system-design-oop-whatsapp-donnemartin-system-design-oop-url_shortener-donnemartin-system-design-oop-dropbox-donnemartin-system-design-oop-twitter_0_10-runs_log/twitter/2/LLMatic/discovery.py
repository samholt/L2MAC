from collections import Counter
from user import users_db
from post import posts_db


def get_trending_topics() -> list:
	# Get all hashtags from all posts
	hashtags = [word for post in posts_db.values() for word in post.content.split() if word.startswith('#')]
	# Count the occurrences of each hashtag
	hashtag_counts = Counter(hashtags)
	# Get the top 10 trending hashtags
	trending_topics = hashtag_counts.most_common(10)
	return trending_topics


def recommend_users(username: str) -> list:
	if username in users_db:
		user = users_db[username]
		# Get the interests of the user (hashtags they have used)
		interests = [word for post in posts_db.values() if post.user.username == username for word in post.content.split() if word.startswith('#')]
		# Get the users who have used the same hashtags
		recommended_users = [post.user.username for post in posts_db.values() for word in post.content.split() if word in interests and post.user.username != username]
		# Remove duplicates
		recommended_users = list(set(recommended_users))
		return recommended_users
	else:
		return 'User not found'
