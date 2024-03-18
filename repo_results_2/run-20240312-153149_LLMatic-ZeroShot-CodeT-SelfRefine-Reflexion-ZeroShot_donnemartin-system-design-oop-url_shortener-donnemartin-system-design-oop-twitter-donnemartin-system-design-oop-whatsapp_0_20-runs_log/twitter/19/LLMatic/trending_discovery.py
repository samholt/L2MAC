import collections


class Trending:
	def __init__(self):
		self.posts = []

	def add_post(self, post):
		self.posts.append(post)

	def get_trending_topics(self):
		topics = []
		for post in self.posts:
			topics.extend(post.content.split())
		counter = collections.Counter(topics)
		return counter.most_common(10)


class Discovery:
	def __init__(self, users_db):
		self.users_db = users_db

	def recommend_users(self, username):
		user = self.users_db[username]
		recommendations = []
		for other_username, other_user in self.users_db.items():
			if other_username != username and len(set(user['following']).intersection(set(other_user['followers']))) > 0:
				recommendations.append(other_username)
		return recommendations[:10]
