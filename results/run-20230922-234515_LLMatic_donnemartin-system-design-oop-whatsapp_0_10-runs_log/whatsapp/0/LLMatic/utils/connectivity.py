import requests

# In-memory queue for storing messages when the user is offline.
# In a real-world application, a more robust and persistent queuing system like Redis or RabbitMQ should be used.
message_queue = {}

def is_connected():
	try:
		requests.get('http://google.com', timeout=5)
		return True
	except requests.exceptions.RequestException:
		return False

def queue_message(user_id, message):
	if user_id not in message_queue:
		message_queue[user_id] = []
	message_queue[user_id].append(message)

def send_queued_messages(user_id):
	if user_id in message_queue:
		messages = message_queue[user_id]
		del message_queue[user_id]
		return messages
	return []
