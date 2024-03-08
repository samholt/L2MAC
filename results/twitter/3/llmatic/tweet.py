class Tweet:
	def __init__(self, user, content):
		self.user = user
		self.content = content
		self.replies = []
		self.mentions = []
		self.privacy = 'public'

	def reply(self, user, content):
		reply = Tweet(user, content)
		self.replies.append(reply)
		return reply

	def set_privacy(self, privacy):
		self.privacy = privacy

	def get_privacy(self):
		return self.privacy
