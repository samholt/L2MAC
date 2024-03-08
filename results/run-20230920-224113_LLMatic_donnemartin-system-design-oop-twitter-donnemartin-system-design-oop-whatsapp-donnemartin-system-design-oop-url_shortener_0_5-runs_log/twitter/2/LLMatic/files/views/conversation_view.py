from models.conversation import Conversation


class ConversationView:
	@staticmethod
	def display_conversation(conversation: Conversation):
		for tweet in conversation.tweets:
			print(f'{tweet.user.username}: {tweet.content}')
