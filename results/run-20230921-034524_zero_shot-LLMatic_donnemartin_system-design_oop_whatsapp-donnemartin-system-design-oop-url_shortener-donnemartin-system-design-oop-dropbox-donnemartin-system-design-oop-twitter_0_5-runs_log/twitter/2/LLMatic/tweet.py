class Tweet:
	def __init__(self, user, content, privacy):
		self.user = user
		self.content = content
		self.privacy = privacy
		self.replies = []
		self.conversation_id = None

	def set_privacy(self, privacy):
		self.privacy = privacy

	def group_by_conversation(self, conversation_id):
		self.conversation_id = conversation_id
