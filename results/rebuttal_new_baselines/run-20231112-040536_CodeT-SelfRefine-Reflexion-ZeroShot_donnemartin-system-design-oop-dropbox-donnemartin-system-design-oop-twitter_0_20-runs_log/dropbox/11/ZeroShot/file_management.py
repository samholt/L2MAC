from dataclasses import dataclass

@dataclass
class File:
	name: str
	size: int
	type: str
	versions: list

files = {}


def upload_file(data):
	file = File(**data)
	files[file.name] = file
	return {'message': 'File uploaded successfully'}

def download_file(data):
	file = files.get(data['name'])
	if file:
		return {'file': file}
	return {'message': 'File not found'}

def organize_file(data):
	file = files.get(data['name'])
	if file:
		file.name = data['new_name']
		return {'message': 'File organized successfully'}
	return {'message': 'File not found'}

def version_file(data):
	file = files.get(data['name'])
	if file:
		return {'versions': file.versions}
	return {'message': 'File not found'}
