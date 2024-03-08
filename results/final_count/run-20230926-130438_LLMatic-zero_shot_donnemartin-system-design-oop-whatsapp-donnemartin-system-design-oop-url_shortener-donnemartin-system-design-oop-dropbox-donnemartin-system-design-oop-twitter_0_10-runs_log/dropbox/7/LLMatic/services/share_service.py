class ShareService:
	def __init__(self):
		self.shared_files = {}
		self.shared_folders = {}

	def share_file(self, file_id, user_id):
		# Create a shareable link
		link = f'http://fileshare.com/{file_id}'

		# Send the link to the User's email
		# In a real-world application, we would use an email service here
		print(f'Sent link: {link} to user: {user_id}')

		# Store the shared file
		self.shared_files[file_id] = user_id

	def share_folder(self, folder_id, user_id, permissions):
		# Create a shareable link
		link = f'http://fileshare.com/{folder_id}'

		# Send the link to the User's email
		# In a real-world application, we would use an email service here
		print(f'Sent link: {link} to user: {user_id} with permissions: {permissions}')

		# Store the shared folder and permissions
		self.shared_folders[folder_id] = {'user_id': user_id, 'permissions': permissions}

	def get_shared_files(self):
		return self.shared_files

	def get_shared_folders(self):
		return self.shared_folders
