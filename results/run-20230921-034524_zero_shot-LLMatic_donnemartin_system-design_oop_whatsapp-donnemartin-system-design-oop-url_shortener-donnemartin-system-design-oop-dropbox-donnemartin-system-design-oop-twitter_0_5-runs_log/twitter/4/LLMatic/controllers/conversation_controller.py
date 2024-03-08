from models.conversation import Conversation


class ConversationController:
	def __init__(self):
		self.conversations = []

	def create_conversation(self, tweets):
		conversation = Conversation(tweets)
		self.conversations.append(conversation)
		return conversation

	def get_conversation(self, id: int):
		if id < len(self.conversations):
			return self.conversations[id]
		return None

	def delete_conversation(self, id: int):
		conversation = self.get_conversation(id)
		if conversation:
			self.conversations.remove(conversation)
			return conversation
		return None
