class PostManagement:
	def __init__(self):
		self.posts = {}

	def create_post(self, user_id, post_content, image=None):
		if user_id not in self.posts:
			self.posts[user_id] = []
		new_post = {'content': post_content, 'image': image, 'likes': 0, 'retweets': 0, 'replies': []}
		self.posts[user_id].append(new_post)
		return new_post

	def delete_post(self, user_id, post_index):
		if user_id in self.posts and post_index < len(self.posts[user_id]):
			return self.posts[user_id].pop(post_index)
		return None

	def like_post(self, user_id, post_index):
		if user_id in self.posts and post_index < len(self.posts[user_id]):
			self.posts[user_id][post_index]['likes'] += 1
			return self.posts[user_id][post_index]
		return None

	def retweet_post(self, user_id, post_index):
		if user_id in self.posts and post_index < len(self.posts[user_id]):
			self.posts[user_id][post_index]['retweets'] += 1
			return self.posts[user_id][post_index]
		return None

	def reply_to_post(self, user_id, post_index, reply_content):
		if user_id in self.posts and post_index < len(self.posts[user_id]):
			new_reply = {'content': reply_content, 'likes': 0, 'retweets': 0, 'replies': []}
			self.posts[user_id][post_index]['replies'].append(new_reply)
			return new_reply
		return None

	def search_posts(self, keyword):
		result = []
		for user_id in self.posts:
			for post in self.posts[user_id]:
				if keyword in post['content']:
					result.append(post)
		return result

	def filter_posts_by_hashtag(self, hashtag):
		result = []
		for user_id in self.posts:
			for post in self.posts[user_id]:
				if hashtag in post['content']:
					result.append(post)
		return result

	def filter_posts_by_user_mention(self, user_id):
		result = []
		for user in self.posts:
			for post in self.posts[user]:
				if '@' + user_id in post['content']:
					result.append(post)
		return result

	def filter_posts_by_trending_topic(self, topic):
		result = []
		for user_id in self.posts:
			for post in self.posts[user_id]:
				if topic in post['content']:
					result.append(post)
		return result
