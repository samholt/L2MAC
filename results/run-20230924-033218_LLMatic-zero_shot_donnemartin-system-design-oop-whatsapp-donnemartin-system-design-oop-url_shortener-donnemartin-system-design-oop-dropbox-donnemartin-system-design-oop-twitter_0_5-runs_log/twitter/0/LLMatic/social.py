from models import Message

# Mock database
messages_db = {}


def send_message(sender_id, receiver_id, text):
	message = Message(len(messages_db) + 1, sender_id, receiver_id, text)
	messages_db[message.id] = message
	return message


def get_conversation(user1_id, user2_id):
	return sorted([message for message in messages_db.values() if (message.sender_id == user1_id and message.receiver_id == user2_id) or (message.sender_id == user2_id and message.receiver_id == user1_id)], key=lambda message: message.timestamp)

