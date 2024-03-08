from dataclasses import dataclass

@dataclass
class SharedFile:
	name: str
	url: str
	expiry_date: str
	password: str

shared_files = {}


def share_file(data):
	shared_file = SharedFile(**data)
	shared_files[shared_file.name] = shared_file
	return {'message': 'File shared successfully'}

def shared_folder(data):
	return {'message': 'Folder shared successfully'}
