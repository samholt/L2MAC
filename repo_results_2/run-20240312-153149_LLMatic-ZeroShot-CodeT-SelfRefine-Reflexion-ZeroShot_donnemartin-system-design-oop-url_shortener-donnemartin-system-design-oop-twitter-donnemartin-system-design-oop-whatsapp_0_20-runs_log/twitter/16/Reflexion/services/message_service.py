from models.message import Message

messages = {}

def send_message(sender, receiver, content):
	message = Message(sender, receiver, content)
	messages[(sender.email, receiver.email)] = message
	return message

def get_message(sender, receiver):
	return messages.get((sender.email, receiver.email), None)
