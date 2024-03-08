from dataclasses import dataclass

@dataclass
class Share:
	link: str
	expiry_date: str
	password: str

shares = {}


def share_link(data):
	share = Share(**data)
	shares[share.link] = share
	return {'message': 'Link shared successfully'}, 201

def shared_folder(data):
	share = Share(**data)
	shares[share.link] = share
	return {'message': 'Folder shared successfully'}, 201
