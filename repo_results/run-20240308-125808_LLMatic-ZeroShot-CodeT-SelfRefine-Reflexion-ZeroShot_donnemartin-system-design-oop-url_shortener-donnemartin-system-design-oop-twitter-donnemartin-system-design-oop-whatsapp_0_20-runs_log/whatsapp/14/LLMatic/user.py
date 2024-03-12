class Status:
	def __init__(self, content, visibility_duration, visibility_setting):
		self.content = content
		self.visibility_duration = visibility_duration
		self.visibility_setting = visibility_setting


class User:
	def __init__(self, email, password, profile_picture=None, status_message=None, privacy_setting='public'):
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.status_message = status_message
		self.privacy_setting = privacy_setting
		self.statuses = []
		self.online_status = False
		self.message_queue = []

	def set_profile_picture(self, profile_picture):
		self.profile_picture = profile_picture

	def set_status_message(self, status_message):
		self.status_message = status_message

	def set_privacy_setting(self, privacy_setting):
		self.privacy_setting = privacy_setting

	def post_status(self, content, visibility_duration, visibility_setting):
		status = Status(content, visibility_duration, visibility_setting)
		self.statuses.append(status)

	def get_statuses(self):
		return self.statuses

	def set_online_status(self, status):
		self.online_status = status
		if self.online_status:
			self.send_queued_messages()

	def get_online_status(self):
		return self.online_status

	def queue_message(self, message):
		self.message_queue.append(message)

	def send_queued_messages(self):
		for message in self.message_queue:
			message.send_message()
		self.message_queue = []


class UserDatabase:
	def __init__(self):
		self.users = {}

	def sign_up(self, email, password):
		if email in self.users:
			return 'User already exists'
		else:
			self.users[email] = User(email, password)
			return 'User registered successfully'

	def password_recovery(self, email):
		if email in self.users:
			return 'Password recovery link sent to ' + email
		else:
			return 'User does not exist'
