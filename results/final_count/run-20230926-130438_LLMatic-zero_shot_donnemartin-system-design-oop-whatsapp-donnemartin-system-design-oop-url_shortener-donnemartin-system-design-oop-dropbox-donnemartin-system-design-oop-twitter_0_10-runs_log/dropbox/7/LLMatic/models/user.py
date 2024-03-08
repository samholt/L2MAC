class User:
	def __init__(self, id, name, email, password, profile_picture, storage_used):
		self.id = id
		self.name = name
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.storage_used = storage_used
		self.activity_log = []

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password

	def get_profile_picture(self):
		return self.profile_picture

	def get_storage_used(self):
		return self.storage_used

	def get_activity_log(self):
		return self.activity_log

	def set_name(self, name):
		self.name = name

	def set_email(self, email):
		self.email = email

	def set_password(self, password):
		self.password = password

	def set_profile_picture(self, profile_picture):
		self.profile_picture = profile_picture

	def set_storage_used(self, storage_used):
		self.storage_used = storage_used

	def add_to_activity_log(self, action):
		self.activity_log.append(action)
