from dataclasses import dataclass

@dataclass
class File:
	name: str
	type: str
	size: int
	versions: list

files = {}


def upload(data):
	file = File(**data)
	files[file.name] = file
	return {'message': 'File uploaded successfully'}, 201

def download(data):
	file = files.get(data['name'])
	if file:
		return file.__dict__, 200
	else:
		return {'message': 'File not found'}, 404

def organize(data):
	file = files.get(data['name'])
	if file:
		file.name = data.get('new_name', file.name)
		return {'message': 'File organized successfully'}, 200
	else:
		return {'message': 'File not found'}, 404

def get_versions():
	return {file.name: file.versions for file in files.values()}, 200

def restore_version(data):
	file = files.get(data['name'])
	if file and data['version'] in file.versions:
		file.versions.remove(data['version'])
		file.versions.append(data['version'])
		return {'message': 'Version restored successfully'}, 200
	else:
		return {'message': 'File or version not found'}, 404
