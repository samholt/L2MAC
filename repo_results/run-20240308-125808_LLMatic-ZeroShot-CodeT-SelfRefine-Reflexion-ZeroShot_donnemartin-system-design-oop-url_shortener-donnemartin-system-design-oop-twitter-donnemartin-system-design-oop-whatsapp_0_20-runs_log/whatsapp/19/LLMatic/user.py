class User:
	def __init__(self, email, password, profile_picture=None, status_message=None, privacy_settings=None):
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.status_message = status_message
		self.privacy_settings = privacy_settings

	def sign_up(self, email, password):
		self.email = email
		self.password = password
		return 'User signed up successfully'

	def password_recovery(self, email):
		if self.email == email:
			return 'Password recovery link has been sent to your email'
		else:
			return 'Email not found'

	def set_profile_picture(self, picture_file):
		self.profile_picture = picture_file
		return 'Profile picture set successfully'

	def set_status_message(self, status_message):
		self.status_message = status_message
		return 'Status message set successfully'

	def manage_privacy_settings(self, privacy_settings):
		self.privacy_settings = privacy_settings
		return 'Privacy settings updated successfully'


class Contact:
	def __init__(self, user, blocked=False):
		self.user = user
		self.blocked = blocked

	def block_contact(self, user):
		if self.user == user:
			self.blocked = True
			return 'Contact blocked successfully'
		else:
			return 'User not found'

	def unblock_contact(self, user):
		if self.user == user:
			self.blocked = False
			return 'Contact unblocked successfully'
		else:
			return 'User not found'

	def create_group(self, group_details):
		self.group = group_details
		return 'Group created successfully'

	def edit_group(self, group_details):
		self.group = group_details
		return 'Group edited successfully'

	def manage_group(self, group_details):
		self.group = group_details
		return 'Group managed successfully'
