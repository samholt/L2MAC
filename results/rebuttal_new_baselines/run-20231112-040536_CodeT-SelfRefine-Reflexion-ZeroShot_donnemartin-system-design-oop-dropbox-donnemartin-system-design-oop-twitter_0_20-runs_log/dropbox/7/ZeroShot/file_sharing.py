from dataclasses import dataclass

@dataclass
class Share:
	file_name: str
	shared_with: list

shares = {}


def share_file(data):
	share = Share(**data)
	shares[share.file_name] = share
	return {'message': 'File shared successfully'}
