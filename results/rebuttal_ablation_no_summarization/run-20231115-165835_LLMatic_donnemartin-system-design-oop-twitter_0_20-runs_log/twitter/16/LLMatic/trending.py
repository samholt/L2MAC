import re
from collections import Counter
from post import Post


class Trending:
	def __init__(self):
		self.post = Post()

	def get_trending_topics(self):
		all_posts = self.post.database.values()
		all_text = [post['text'] for post in all_posts]
		all_words = ' '.join(all_text).split()
		hashtags = [word for word in all_words if word.startswith('#')]
		trending = Counter(hashtags).most_common(10)
		return [topic[0] for topic in trending]

	def recommend_users(self, user):
		# Mock database of users and their followers
		user_database = {
			'user1': ['user2', 'user3'],
			'user2': ['user1', 'user3'],
			'user3': ['user1', 'user2']
		}

		# Get the followers of the current user
		current_user_followers = set(user_database.get(user, []))

		# Get the posts of the current user
		current_user_posts = [post for post in self.post.database.values() if post['user'] == user]

		# Get the hashtags used by the current user
		current_user_hashtags = set()
		for post in current_user_posts:
			current_user_hashtags.update(re.findall(r'#\w+', post['text']))

		# Recommend users based on interests, activity, and mutual followers
		recommended_users = []
		for other_user, followers in user_database.items():
			if other_user == user:
				continue

			# Interests: Check if the other user has used any of the same hashtags
			other_user_posts = [post for post in self.post.database.values() if post['user'] == other_user]
			other_user_hashtags = set()
			for post in other_user_posts:
				other_user_hashtags.update(re.findall(r'#\w+', post['text']))
			if not current_user_hashtags.intersection(other_user_hashtags):
				continue

			# Activity: Check if the other user has at least as many posts as the current user
			if len(other_user_posts) < len(current_user_posts):
				continue

			# Mutual followers: Check if the current user and the other user have any mutual followers
			mutual_followers = current_user_followers.intersection(set(followers))
			if not mutual_followers:
				continue

			recommended_users.append(other_user)

		return recommended_users
