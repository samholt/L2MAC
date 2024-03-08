class Status:
	def __init__(self):
		self.status_db = {}
		self.message_queue = {}
		self.user_status = {}

	def post_status(self, user_id, image_file, visibility):
		status_id = len(self.status_db) + 1
		self.status_db[status_id] = {'user_id': user_id, 'image_file': image_file, 'visibility': visibility}
		return 'Status posted successfully'

	def control_visibility(self, user_id, status_id, visibility):
		if self.status_db.get(status_id) and self.status_db[status_id]['user_id'] == user_id:
			self.status_db[status_id]['visibility'] = visibility
			return 'Visibility updated successfully'
		else:
			return 'Status not found or user not authorized'

	def queue_message(self, sender_id, receiver_id, message):
		if self.user_status.get(receiver_id) == 'offline':
			if self.message_queue.get(receiver_id) is None:
				self.message_queue[receiver_id] = []
			self.message_queue[receiver_id].append({'sender_id': sender_id, 'message': message})
			return 'Message queued'
		else:
			return 'User is online'

	def display_status(self, user_id):
		return self.user_status.get(user_id, 'offline')
