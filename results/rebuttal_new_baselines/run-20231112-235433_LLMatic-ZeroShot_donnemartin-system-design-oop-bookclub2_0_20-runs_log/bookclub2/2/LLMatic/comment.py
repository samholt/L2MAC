class Comment:
	def __init__(self, id, content, user):
		self.id = id
		self.content = content
		self.user = user

	def create_comment(self, id, content, user):
		self.id = id
		self.content = content
		self.user = user

	def edit_comment(self, new_content):
		self.content = new_content

	def get_comment_info(self):
		return {'id': self.id, 'content': self.content, 'user': self.user}
