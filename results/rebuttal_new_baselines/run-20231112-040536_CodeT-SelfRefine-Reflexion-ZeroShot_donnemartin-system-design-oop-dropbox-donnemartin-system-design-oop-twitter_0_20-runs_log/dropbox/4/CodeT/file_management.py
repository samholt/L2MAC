from dataclasses import dataclass

@dataclass
class File:
	name: str
	size: int
	type: str
	versions: list

files = {}


def upload(data):
	file = File(**data)
	files[file.name] = file
	return {'message': 'File uploaded successfully'}


def download(data):
	file = files.get(data['name'])
	if file:
		return file.__dict__
	return {'message': 'File not found'}


def organize(data):
	file = files.get(data['name'])
	if file:
		file.name = data['new_name']
		return {'message': 'File organized successfully'}
	return {'message': 'File not found'}


def versioning(data):
	file = files.get(data['name'])
	if file:
		return {'versions': file.versions}
	return {'message': 'File not found'}
