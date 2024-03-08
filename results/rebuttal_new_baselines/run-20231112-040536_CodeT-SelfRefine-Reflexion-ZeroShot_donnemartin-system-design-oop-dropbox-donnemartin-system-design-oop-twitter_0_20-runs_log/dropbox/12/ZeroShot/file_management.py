from dataclasses import dataclass

@dataclass
class File:
	name: str
	type: str
	size: int
	versions: list

files = {}


def upload_file(data):
	file = File(**data)
	files[file.name] = file
	return {'status': 'success', 'message': 'File uploaded successfully'}

def download_file(data):
	file = files.get(data['name'])
	if file:
		return {'status': 'success', 'data': file.__dict__}
	return {'status': 'error', 'message': 'File not found'}

def organize_file(data):
	file = files.get(data['name'])
	if file:
		file.name = data['new_name']
		return {'status': 'success', 'message': 'File organized successfully'}
	return {'status': 'error', 'message': 'File not found'}

def version_file(data):
	file = files.get(data['name'])
	if file:
		return {'status': 'success', 'data': file.versions}
	return {'status': 'error', 'message': 'File not found'}
