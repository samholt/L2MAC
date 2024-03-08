from dataclasses import dataclass

@dataclass
class File:
	name: str
	size: int
	type: str
	location: str

files = {}


def upload_file(data):
	file = File(**data)
	files[file.name] = file
	return {'message': 'File uploaded successfully'}, 201

def download_file(data):
	file = files.get(data['name'])
	if file:
		return {'file': file}, 200
	return {'message': 'File not found'}, 404

def create_folder(data):
	# Placeholder for folder creation
	return {'message': 'Folder created successfully'}, 201

def rename_file(data):
	file = files.get(data['old_name'])
	if file:
		file.name = data['new_name']
		return {'message': 'File renamed successfully'}, 200
	return {'message': 'File not found'}, 404

def move_file(data):
	file = files.get(data['name'])
	if file:
		file.location = data['new_location']
		return {'message': 'File moved successfully'}, 200
	return {'message': 'File not found'}, 404

def delete_file(data):
	file = files.get(data['name'])
	if file:
		del files[file.name]
		return {'message': 'File deleted successfully'}, 200
	return {'message': 'File not found'}, 404
