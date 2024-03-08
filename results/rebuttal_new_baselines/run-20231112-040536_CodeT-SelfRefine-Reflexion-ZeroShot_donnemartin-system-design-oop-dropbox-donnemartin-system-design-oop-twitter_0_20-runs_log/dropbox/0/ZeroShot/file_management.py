from dataclasses import dataclass

@dataclass
class File:
	name: str
	type: str
	size: int
	content: str

files = {}


def upload_file(data):
	file = File(**data)
	files[file.name] = file
	return {'message': 'File uploaded successfully'}

def download_file(data):
	file = files.get(data['name'])
	if file:
		return {'name': file.name, 'type': file.type, 'size': file.size, 'content': file.content}
	return {'message': 'File not found'}

def organize_file(data):
	file = files.get(data['name'])
	if file:
		file.name = data['new_name']
		return {'message': 'File organized successfully'}
	return {'message': 'File not found'}

def file_versioning(data):
	file = files.get(data['name'])
	if file:
		return {'name': file.name, 'type': file.type, 'size': file.size, 'content': file.content}
	return {'message': 'File not found'}
