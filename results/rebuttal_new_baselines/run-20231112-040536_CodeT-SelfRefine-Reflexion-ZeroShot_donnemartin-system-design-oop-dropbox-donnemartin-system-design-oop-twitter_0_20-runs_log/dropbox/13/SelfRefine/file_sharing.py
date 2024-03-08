from dataclasses import dataclass

@dataclass
class Share:
	file_name: str
	shared_with: list
	permissions: dict

shares = {}


def share_link(data):
	share = Share(**data)
	shares[share.file_name] = share
	return {'message': 'Link shared successfully'}

def shared_folder(data):
	share = shares.get(data['file_name'])
	if share:
		share.shared_with.append(data['email'])
		return {'message': 'Folder shared successfully'}
	return {'message': 'Share not found'}
