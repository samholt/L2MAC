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
	return {'message': 'File uploaded successfully'}, 201

def download_file(data):
	file = files.get(data['name'])
	if file:
		return file.__dict__, 200
	return {'message': 'File not found'}, 404

def organize_file(data):
	file = files.get(data['name'])
	if file:
		file.name = data['new_name']
		return {'message': 'File organized successfully'}, 200
	return {'message': 'File not found'}, 404

def version_file(data):
	file = files.get(data['name'])
	if file:
		return {'versions': file.versions}, 200
	return {'message': 'File not found'}, 404
