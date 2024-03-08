from models.file import File
from services.file_service import files_db

# Mock database
shares_db = {}

# Activity log
activity_log = []

def share_file(file_id, user_id, target_user_id):
	file = files_db.get(file_id)
	if file and file.owner == user_id:
		activity_log.append(f'File with id {file.id} shared by user {user_id} with user {target_user_id}')
		file.shared_with.append(target_user_id)

def get_activity_log():
	return activity_log
