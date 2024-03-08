from models.conversation import Conversation
from views.conversation_view import ConversationView


class ConversationController:
	@staticmethod
	def create_conversation(users, tweets):
		conversation = Conversation(users, tweets)
		ConversationView.display_conversation(conversation)
		return conversation
