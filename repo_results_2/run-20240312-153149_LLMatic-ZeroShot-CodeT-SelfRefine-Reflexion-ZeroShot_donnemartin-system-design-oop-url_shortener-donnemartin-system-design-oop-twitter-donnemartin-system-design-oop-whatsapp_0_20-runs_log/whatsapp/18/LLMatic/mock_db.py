import datetime

class MockDB:
	def __init__(self):
		self.users = {}
		self.groups = {}
		self.statuses = {}
		self.offline_messages = {}

	def add_user(self, email, password):
		self.users[email] = {'email': email, 'password': password, 'status': '', 'picture': '', 'last_activity': None}

	def get_user(self, email, password=None):
		user = self.users.get(email)
		if password is None:
			return user
		if user is not None and user['password'] == password:
			return user

	def set_user_picture(self, email, picture):
		if email in self.users:
			self.users[email]['picture'] = picture

	def set_user_status_message(self, email, message):
		if email in self.users:
			self.users[email]['status'] = message

	def update_user_privacy_settings(self, email, settings):
		if email in self.users:
			self.users[email]['privacy'] = settings

	def block_contact(self, email, contact_email):
		if email in self.users:
			self.users[email].setdefault('blocked', []).append(contact_email)

	def unblock_contact(self, email, contact_email):
		if email in self.users and contact_email in self.users[email].get('blocked', []):
			self.users[email]['blocked'].remove(contact_email)

	def create_group(self, email, group_name, members):
		if email in self.users:
			self.groups[group_name] = {'name': group_name, 'members': members, 'messages': []}

	def get_group(self, group_name):
		return self.groups.get(group_name)

	def edit_group(self, email, group_name, members):
		if email in self.users and group_name in self.groups:
			self.groups[group_name]['members'] = members

	def add_group_admin(self, email, group_name, admin_email):
		if email in self.users and group_name in self.groups:
			self.groups[group_name].setdefault('admins', []).append(admin_email)

	def remove_group_admin(self, email, group_name, admin_email):
		if email in self.users and group_name in self.groups and admin_email in self.groups[group_name].get('admins', []):
			self.groups[group_name]['admins'].remove(admin_email)

	def add_message(self, sender_id, recipient_id, message):
		if sender_id in self.users and recipient_id in self.users:
			self.users[recipient_id].setdefault('messages', []).append({'sender': sender_id, 'text': message})

	def update_read_receipt(self, sender_id, recipient_id):
		if sender_id in self.users and recipient_id in self.users:
			for message in self.users[recipient_id].get('messages', []):
				if message['sender'] == sender_id:
					message['read'] = True

	def add_image(self, sender_id, recipient_id, image):
		if sender_id in self.users and recipient_id in self.users:
			self.users[recipient_id].setdefault('images', []).append({'sender': sender_id, 'image': image})

	def post_status(self, user_id, image):
		if user_id in self.users:
			self.statuses[user_id] = {'image': image, 'visibility': 'public'}

	def get_status(self, user_id):
		return self.statuses.get(user_id)

	def update_status_visibility(self, user_id, visibility):
		if user_id in self.statuses:
			self.statuses[user_id]['visibility'] = visibility

	def add_offline_message(self, sender_id, recipient_id, message):
		if sender_id in self.users and recipient_id in self.users:
			self.offline_messages.setdefault(recipient_id, []).append({'sender': sender_id, 'text': message})

	def get_offline_messages(self, recipient_id):
		return self.offline_messages.get(recipient_id, [])

	def clear_offline_messages(self, recipient_id):
		if recipient_id in self.offline_messages:
			del self.offline_messages[recipient_id]

	def update_last_activity(self, email):
		if email in self.users:
			self.users[email]['last_activity'] = datetime.datetime.now()

	def get_last_activity(self, email):
		if email in self.users:
			return self.users[email].get('last_activity')

