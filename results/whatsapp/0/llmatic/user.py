class User:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.profile_picture = None
		self.status_message = None
		self.privacy_settings = None
		self.blocked_contacts = []
		self.groups = []

	def sign_up(self, email, password):
		self.email = email
		self.password = password

	def log_in(self, email, password):
		if self.email == email and self.password == password:
			return True
		else:
			return False

	def forgot_password(self, new_password):
		self.password = new_password

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def set_status_message(self, message):
		self.status_message = message

	def set_privacy_settings(self, settings):
		self.privacy_settings = settings

	def block_contact(self, contact):
		self.blocked_contacts.append(contact)

	def unblock_contact(self, contact):
		self.blocked_contacts.remove(contact)

	def create_group(self, group):
		self.groups.append(group)

	def edit_group(self, group, new_group):
		index = self.groups.index(group)
		self.groups[index] = new_group

	def manage_group(self, group):
		return group

def test_user():
	user = User('test@example.com', 'password')

	# Test sign_up method
	user.sign_up('new@example.com', 'new_password')
	assert user.email == 'new@example.com'
	assert user.password == 'new_password'

	# Test log_in method
	assert user.log_in('new@example.com', 'new_password') == True
	assert user.log_in('wrong@example.com', 'wrong_password') == False

	# Test forgot_password method
	user.forgot_password('forgot_password')
	assert user.password == 'forgot_password'

	# Test set_profile_picture method
	user.set_profile_picture('picture.jpg')
	assert user.profile_picture == 'picture.jpg'

	# Test set_status_message method
	user.set_status_message('Hello, world!')
	assert user.status_message == 'Hello, world!'

	# Test set_privacy_settings method
	user.set_privacy_settings('Private')
	assert user.privacy_settings == 'Private'

	# Test block_contact method
	user.block_contact('blocked@example.com')
	assert 'blocked@example.com' in user.blocked_contacts

	# Test unblock_contact method
	user.unblock_contact('blocked@example.com')
	assert 'blocked@example.com' not in user.blocked_contacts

	# Test create_group method
	user.create_group('Group 1')
	assert 'Group 1' in user.groups

	# Test edit_group method
	user.edit_group('Group 1', 'Group 2')
	assert 'Group 1' not in user.groups
	assert 'Group 2' in user.groups

	# Test manage_group method
	assert user.manage_group('Group 2') == 'Group 2'
