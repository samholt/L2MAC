from dataclasses import dataclass

@dataclass
class SharedFile:
	name: str
	shared_with: str

shared_files_db = {}


def share_file(data):
	shared_file = SharedFile(**data)
	shared_files_db[shared_file.name] = shared_file
	return {'status': 'success', 'message': 'File shared successfully'}

def shared_folders(data):
	shared_file = shared_files_db.get(data['name'])
	if shared_file:
		return {'status': 'success', 'data': shared_file.__dict__}
	return {'status': 'error', 'message': 'Shared file not found'}
