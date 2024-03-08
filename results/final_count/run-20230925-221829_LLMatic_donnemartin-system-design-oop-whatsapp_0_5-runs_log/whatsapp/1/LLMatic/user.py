import datetime

class User:
	def __init__(self, email, password, profile_picture=None, status=None, status_expiry=None, status_visibility='public', privacy_settings='public', online_status=False, message_queue=[]):
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.status = status
		self.status_expiry = status_expiry
		self.status_visibility = status_visibility
		self.privacy_settings = privacy_settings
		self.online_status = online_status
		self.message_queue = message_queue

	def set_profile_picture(self, profile_picture):
		self.profile_picture = profile_picture

	def post_status(self, status, duration):
		self.status = status
		self.status_expiry = datetime.datetime.now() + datetime.timedelta(hours=duration)

	def set_status_visibility(self, visibility):
		self.status_visibility = visibility

	def set_privacy_settings(self, privacy_settings):
		self.privacy_settings = privacy_settings

	def set_online_status(self, status):
		self.online_status = status
		if status:
			self.send_queued_messages()

	def queue_message(self, message):
		self.message_queue.append(message)

	def send_queued_messages(self):
		for message in self.message_queue:
			print(f'Sending message: {message}')
		self.message_queue = []

mock_db = {}

def sign_up(email, password):
	if email in mock_db:
		return 'User already exists'
	else:
		mock_db[email] = User(email, password)
		return 'User created successfully'

def forgot_password(email):
	if email in mock_db:
		return 'Reset link has been sent to your email'
	else:
		return 'User does not exist'
