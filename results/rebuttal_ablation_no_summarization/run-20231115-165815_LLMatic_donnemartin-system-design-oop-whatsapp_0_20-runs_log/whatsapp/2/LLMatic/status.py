import time

class Status:
	def __init__(self):
		self.statuses = {}
		self.online_status = {}
		self.message_queue = {}

	def post_status(self, user_id, image, visibility):
		status_id = len(self.statuses) + 1
		self.statuses[status_id] = {
			'user_id': user_id,
			'image': image,
			'visibility': visibility,
			'time_posted': time.time()
		}
		return status_id

	def control_status_visibility(self, status_id, visibility):
		if status_id in self.statuses:
			self.statuses[status_id]['visibility'] = visibility
			return True
		return False

	def display_status(self, user_id):
		if user_id in self.online_status:
			return self.statuses[user_id]['visibility'], self.online_status.get(user_id, 'offline')
		return 'User not found'

	def set_online_status(self, user_id, status):
		self.online_status[user_id] = status
		if status == 'online' and user_id in self.message_queue:
			for message in self.message_queue[user_id]:
				print(f'Sending message: {message}')
			self.message_queue[user_id] = []

	def queue_message(self, sender_id, recipient_id, message):
		if self.online_status.get(recipient_id, 'offline') == 'offline':
			if recipient_id not in self.message_queue:
				self.message_queue[recipient_id] = []
			self.message_queue[recipient_id].append((sender_id, message))
		else:
			print(f'Sending message: {message}')
