from dataclasses import dataclass

@dataclass
class ShareLink:
	url: str
	expiry_date: str
	password: str

share_links = {}

@dataclass
class SharedFolder:
	email: str
	permissions: str

shared_folders = {}


def share_link(data):
	share_link = ShareLink(**data)
	share_links[share_link.url] = share_link
	return {'message': 'Share link created successfully'}, 201

def shared_folder(data):
	shared_folder = SharedFolder(**data)
	shared_folders[shared_folder.email] = shared_folder
	return {'message': 'Shared folder created successfully'}, 201
