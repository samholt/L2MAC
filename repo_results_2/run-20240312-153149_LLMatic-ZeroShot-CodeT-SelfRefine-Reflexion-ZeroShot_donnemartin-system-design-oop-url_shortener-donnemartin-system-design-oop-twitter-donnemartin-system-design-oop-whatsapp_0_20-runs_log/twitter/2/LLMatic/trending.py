from collections import Counter
from post import post_db


def trending(location=None):
	hashtags = []
	for user_posts in post_db.values():
		for post in user_posts:
			words = post.text.split()
			hashtags.extend(word for word in words if word.startswith('#'))
	if location:
		hashtags = [hashtag for hashtag in hashtags if location in hashtag]
	return Counter(hashtags).most_common()
