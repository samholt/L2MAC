class User:
	def __init__(self):
		self.users = {}
		self.profile_pictures = {}
		self.status_messages = {}
		self.privacy_settings = {}
		self.blocked_contacts = {}
		self.online_status = {}

	def sign_up(self, email, password):
		if email in self.users:
			return 'Email already in use'
		self.users[email] = password
		self.online_status[email] = 'offline'
		return 'User registered successfully'

	def forgotten_password(self, email):
		if email not in self.users:
			return 'Email not registered'
		return 'Recovery email sent to ' + email

	def set_profile_picture(self, user_id, image_file):
		self.profile_pictures[user_id] = image_file
		return 'Profile picture updated successfully'

	def set_status_message(self, user_id, status_message):
		self.status_messages[user_id] = status_message
		return 'Status message updated successfully'

	def set_privacy_settings(self, user_id, privacy_setting):
		self.privacy_settings[user_id] = privacy_setting
		return 'Privacy settings updated successfully'

	def block_contact(self, user_id, contact_id):
		if user_id not in self.blocked_contacts:
			self.blocked_contacts[user_id] = []
		self.blocked_contacts[user_id].append(contact_id)
		return 'Contact blocked successfully'

	def unblock_contact(self, user_id, contact_id):
		if user_id in self.blocked_contacts and contact_id in self.blocked_contacts[user_id]:
			self.blocked_contacts[user_id].remove(contact_id)
		return 'Contact unblocked successfully'

	def set_online_status(self, user_id, status):
		self.online_status[user_id] = status
		return 'Online status updated successfully'

	def get_online_status(self, user_id):
		return self.online_status.get(user_id, 'offline')
