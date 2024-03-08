from dataclasses import dataclass

@dataclass
class File:
	name: str
	type: str
	size: int
	content: str
	versions: list

files = {}


def upload(data):
	file = File(**data)
	files[file.name] = file
	return {'status': 'success', 'message': 'File uploaded successfully'}

def download(data):
	file = files.get(data['name'])
	if file:
		return {'status': 'success', 'content': file.content}
	else:
		return {'status': 'error', 'message': 'File not found'}

def organize(data):
	file = files.get(data['old_name'])
	if file:
		file.name = data['new_name']
		return {'status': 'success', 'message': 'File organized successfully'}
	else:
		return {'status': 'error', 'message': 'File not found'}

def get_versions(data):
	file = files.get(data['name'])
	if file:
		return {'status': 'success', 'versions': file.versions}
	else:
		return {'status': 'error', 'message': 'File not found'}

def restore_version(data):
	file = files.get(data['name'])
	if file and data['version'] in file.versions:
		file.content = data['version']
		return {'status': 'success', 'message': 'Version restored successfully'}
	else:
		return {'status': 'error', 'message': 'File or version not found'}
