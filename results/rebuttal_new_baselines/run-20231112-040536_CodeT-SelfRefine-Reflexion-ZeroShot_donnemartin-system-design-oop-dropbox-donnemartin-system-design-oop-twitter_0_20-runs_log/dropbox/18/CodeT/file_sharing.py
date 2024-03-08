from dataclasses import dataclass

@dataclass
class Share:
	file_name: str
	shared_with: list
	permissions: dict

shares = {}


def share(data):
	share = Share(**data)
	shares[share.file_name] = share
	return {'message': 'File shared successfully'}, 201
