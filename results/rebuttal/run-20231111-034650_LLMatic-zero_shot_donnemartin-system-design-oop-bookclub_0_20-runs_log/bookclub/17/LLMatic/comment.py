class Comment:
	def __init__(self):
		self.comments = {}

	def post_comment(self, comment_id, comment_data):
		self.comments[comment_id] = comment_data

	def get_comment(self, comment_id):
		return self.comments.get(comment_id, None)

	def update_comment(self, comment_id, comment_data):
		if comment_id in self.comments:
			self.comments[comment_id] = comment_data

	def delete_comment(self, comment_id):
		if comment_id in self.comments:
			del self.comments[comment_id]
