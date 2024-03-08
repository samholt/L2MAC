class Discussion:
	def __init__(self):
		self.discussions = {}

	def create_discussion(self, discussion_id, discussion_data):
		self.discussions[discussion_id] = discussion_data

	def get_discussion(self, discussion_id):
		return self.discussions.get(discussion_id, None)

	def update_discussion(self, discussion_id, discussion_data):
		if discussion_id in self.discussions:
			self.discussions[discussion_id] = discussion_data

	def delete_discussion(self, discussion_id):
		if discussion_id in self.discussions:
			del self.discussions[discussion_id]
