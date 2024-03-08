from dataclasses import dataclass

@dataclass
class File:
	name: str
	type: str
	size: int
	content: str
	version: int = 1

files_db = {}


def upload_file(data):
	file = File(**data)
	files_db[file.name] = file
	return {'status': 'success', 'message': 'File uploaded successfully'}

def download_file(data):
	file = files_db.get(data['name'])
	if file:
		return {'status': 'success', 'data': file.__dict__}
	return {'status': 'error', 'message': 'File not found'}

def organize_file(data):
	file = files_db.get(data['name'])
	if file:
		file.name = data.get('new_name', file.name)
		return {'status': 'success', 'message': 'File organized successfully'}
	return {'status': 'error', 'message': 'File not found'}

def file_versioning(data):
	file = files_db.get(data['name'])
	if file:
		new_file = File(name=file.name, type=file.type, size=file.size, content=file.content, version=file.version+1)
		files_db[new_file.name] = new_file
		return {'status': 'success', 'data': new_file.__dict__}
	return {'status': 'error', 'message': 'File not found'}
