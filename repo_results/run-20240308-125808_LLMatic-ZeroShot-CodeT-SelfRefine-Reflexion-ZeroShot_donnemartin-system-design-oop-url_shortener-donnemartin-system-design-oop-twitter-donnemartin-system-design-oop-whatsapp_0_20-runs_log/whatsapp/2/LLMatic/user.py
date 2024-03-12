import time

class User:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.profile_picture = None
		self.status_message = None
		self.privacy_settings = None
		self.statuses = []
		self.is_online = False
		self.message_queue = []

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def get_profile_picture(self):
		return self.profile_picture

	def set_status_message(self, message):
		self.status_message = message

	def get_status_message(self):
		return self.status_message

	def set_privacy_settings(self, settings):
		self.privacy_settings = settings

	def get_privacy_settings(self):
		return self.privacy_settings

	def post_status(self, image, visibility):
		status = {'image': image, 'posted_at': time.time(), 'visibility': visibility}
		self.statuses.append(status)

	def get_statuses(self):
		current_time = time.time()
		valid_statuses = [status for status in self.statuses if current_time - status['posted_at'] <= 24*60*60]
		return valid_statuses

	def set_online_status(self, status):
		self.is_online = status

	def get_online_status(self):
		return self.is_online

	def add_to_message_queue(self, message):
		self.message_queue.append(message)

	def get_message_queue(self):
		return self.message_queue

	def clear_message_queue(self):
		self.message_queue = []

	def receive_message(self, message):
		if self.is_online:
			print(f'Message from {message["sender"]}: {message["content"]}')
		else:
			self.add_to_message_queue(message)
