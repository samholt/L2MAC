class UserProfile:
	def __init__(self):
		self.database = {}

	def set_profile_picture(self, user_id, image_file):
		if user_id in self.database:
			self.database[user_id]['profile_picture'] = image_file
		else:
			self.database[user_id] = {'profile_picture': image_file}

	def set_status_message(self, user_id, status_message):
		if user_id in self.database:
			self.database[user_id]['status_message'] = status_message
		else:
			self.database[user_id] = {'status_message': status_message}

	def manage_privacy_settings(self, user_id, privacy_setting):
		if user_id in self.database:
			self.database[user_id]['privacy_setting'] = privacy_setting
		else:
			self.database[user_id] = {'privacy_setting': privacy_setting}
