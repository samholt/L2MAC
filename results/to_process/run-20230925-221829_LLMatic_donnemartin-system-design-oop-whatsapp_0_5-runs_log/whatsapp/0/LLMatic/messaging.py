import hashlib

# Mock database
messages_db = {}
media_db = {}
offline_messages_db = {}


def send_message(sender_id, receiver_id, message):
	message_id = hashlib.md5((sender_id + receiver_id + message).encode()).hexdigest()
	messages_db[message_id] = {'sender_id': sender_id, 'receiver_id': receiver_id, 'message': message, 'read': False}
	return message_id


def receive_messages(user_id):
	return [msg for msg in messages_db.values() if msg['receiver_id'] == user_id]


def handle_read_receipt(message_id):
	if message_id in messages_db:
		messages_db[message_id]['read'] = True
		return True
	return False


def encrypt_message(message):
	return hashlib.md5(message.encode()).hexdigest()


def share_media(sender_id, receiver_id, media):
	media_id = hashlib.md5((sender_id + receiver_id + str(media)).encode()).hexdigest()
	media_db[media_id] = {'sender_id': sender_id, 'receiver_id': receiver_id, 'media': media}
	return media_id


def queue_offline_message(sender_id, receiver_id, message):
	message_id = hashlib.md5((sender_id + receiver_id + message).encode()).hexdigest()
	offline_messages_db[message_id] = {'sender_id': sender_id, 'receiver_id': receiver_id, 'message': message}
	return message_id


def send_offline_messages(user_id):
	messages = [(msg_id, msg) for msg_id, msg in offline_messages_db.items() if msg['receiver_id'] == user_id]
	for msg_id, message in messages:
		send_message(message['sender_id'], message['receiver_id'], message['message'])
		offline_messages_db.pop(msg_id)
	return messages
