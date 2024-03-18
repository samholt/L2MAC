from status import Status

class User:
	def __init__(self, email, password, profile_picture, status_message, privacy_settings):
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.status_message = status_message
		self.privacy_settings = privacy_settings
		self.blocked_contacts = []
		self.groups = {}
		self.statuses = []
		self.is_online = False

	def signup(self, email, password):
		self.email = email
		self.password = password
		return 'User signed up successfully'

	def recover_password(self, email):
		if self.email == email:
			return self.password
		else:
			return 'Email not found'

	def set_profile_picture(self, picture):
		self.profile_picture = picture
		return 'Profile picture set successfully'

	def set_status_message(self, message):
		self.status_message = message
		return 'Status message set successfully'

	def manage_privacy_settings(self, settings):
		self.privacy_settings = settings
		return 'Privacy settings updated successfully'

	def block_contact(self, contact):
		self.blocked_contacts.append(contact)
		return 'Contact blocked successfully'

	def unblock_contact(self, contact):
		self.blocked_contacts.remove(contact)
		return 'Contact unblocked successfully'

	def create_group(self, group_name):
		self.groups[group_name] = []
		return 'Group created successfully'

	def add_contact_to_group(self, group_name, contact):
		self.groups[group_name].append(contact)
		return 'Contact added to group successfully'

	def remove_contact_from_group(self, group_name, contact):
		self.groups[group_name].remove(contact)
		return 'Contact removed from group successfully'

	def delete_group(self, group_name):
		del self.groups[group_name]
		return 'Group deleted successfully'

	def post_status(self, message, visibility):
		status = Status(self, message, visibility)
		self.statuses.append(status)
		return 'Status posted successfully'

	def view_statuses(self):
		visible_statuses = [status for status in self.statuses if status.visibility == 'public' or status.user == self]
		return visible_statuses

	def set_online_status(self, status):
		self.is_online = status
		return 'Online status set successfully'

	def get_online_status(self):
		return self.is_online
