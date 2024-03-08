class Tweet:
	def __init__(self, user, content, privacy):
		self.user = user
		self.content = content
		self.privacy = privacy
		self.replies = []

	def set_privacy(self, privacy):
		self.privacy = privacy

	def get_replies(self):
		return self.replies
