class Search:
	def __init__(self, data):
		self.data = data

	def search_by_keyword(self, keyword):
		results = [item for item in self.data if keyword in item]
		return results

	def filter_by_hashtag(self, hashtag):
		results = [item for item in self.data if '#' + hashtag in item]
		return results

	def filter_by_user_mention(self, username):
		results = [item for item in self.data if '@' + username in item]
		return results

	def filter_by_trending(self, trending_list):
		results = [item for item in self.data if any(trend in item for trend in trending_list)]
		return results
