from file import File

class Service:
	files = {}
	shared_files = {}

	@classmethod
	def upload_file(cls, user_id, file):
		file_id = len(cls.files) + 1
		cls.files[file_id] = File(file_id, user_id, file.read())

	@classmethod
	def view_file(cls, user_id, file_id):
		if file_id in cls.files and (cls.files[file_id].user_id == user_id or user_id in cls.shared_files.get(file_id, [])):
			return cls.files[file_id].read()
		return 'Access denied'

	@classmethod
	def search_files(cls, user_id, query):
		return [file_id for file_id, file in cls.files.items() if file.user_id == user_id and query in file.read()]

	@classmethod
	def share_file(cls, user_id, file_id, recipient_id):
		if file_id in cls.files and cls.files[file_id].user_id == user_id:
			cls.shared_files.setdefault(file_id, []).append(recipient_id)

	@classmethod
	def download_file(cls, user_id, file_id):
		if file_id in cls.files and (cls.files[file_id].user_id == user_id or user_id in cls.shared_files.get(file_id, [])):
			return cls.files[file_id].read()
		return 'Access denied'
