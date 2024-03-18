class Comment:
	def __init__(self, text, user, post):
		self.text = text
		self.user = user
		self.post = post

	def create_comment(self):
		return {'text': self.text, 'user': self.user.username, 'post': self.post.text}
