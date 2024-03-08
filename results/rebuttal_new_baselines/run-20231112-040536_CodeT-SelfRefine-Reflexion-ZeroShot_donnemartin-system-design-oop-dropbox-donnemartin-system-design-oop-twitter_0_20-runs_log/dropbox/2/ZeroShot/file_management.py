from dataclasses import dataclass

@dataclass
class File:
	name: str
	size: int
	type: str
	versions: list = None

files = {}


def upload(data):
	file = File(**data)
	files[file.name] = file
	return {'message': 'File uploaded successfully'}, 201

def download(data):
	file = files.get(data['name'])
	if file:
		return {'file': file}, 200
	return {'message': 'File not found'}, 404

def organize(data):
	file = files.get(data['name'])
	if file:
		file.name = data.get('new_name', file.name)
		return {'message': 'File organized successfully'}, 200
	return {'message': 'File not found'}, 404

def get_versions():
	return {'files': files}, 200

def restore_version(data):
	file = files.get(data['name'])
	if file:
		file.versions = data.get('versions', file.versions)
		return {'message': 'File version restored successfully'}, 200
	return {'message': 'File not found'}, 404
