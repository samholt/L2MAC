from dataclasses import dataclass

@dataclass
class SharedFile:
	name: str
	shared_with: list

shared_files = {}


def share(data):
	shared_file = SharedFile(**data)
	shared_files[shared_file.name] = shared_file
	return {'message': 'File shared successfully'}


def shared_folders(data):
	shared_file = shared_files.get(data['name'])
	if shared_file:
		return shared_file.__dict__
	return {'message': 'Shared file not found'}
