class Tweet:
	def __init__(self, content, user):
		self.content = content
		self.user = user
		self.privacy = 'public'
		self.conversation = None
		self.replies = []

	def set_privacy(self, privacy):
		if privacy in ['public', 'private']:
			self.privacy = privacy
		else:
			raise ValueError('Invalid privacy setting')

	def group_in_conversation(self, conversation):
		self.conversation = conversation
